from google.colab import drive
import libtorrent as lt
import time
import datetime

drive.mount('/content/drive')

!apt install python3-libtorrent

ses = lt.session()
ses.listen_on(6881, 6891)

# Replace with your desired save path and magnet link
save_path = '/content/drive/My Drive/Torrent/'
magnet_link = "YOUR_MAGNET_LINK_HERE"

params = {
    'save_path': save_path,
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True
}

handle = lt.add_magnet_uri(ses, magnet_link, params)
ses.start_dht()

print('Downloading Metadata...')
while not handle.has_metadata():
    time.sleep(1)
print('Got Metadata, starting download...')

while handle.status().state != lt.torrent_status.seeding:
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating']
    print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' %
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
           s.num_peers, state_str[s.state]))
    time.sleep(5)

print(handle.name(), 'COMPLETE')
