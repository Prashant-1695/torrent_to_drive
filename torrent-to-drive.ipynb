# Mount your Google Drive
from google.colab import drive
drive.mount('/content/drive')
# Follow the URL select the required Google Account
# paste the provided Authentication Code

!apt install python3-libtorrent
import libtorrent as lt
import time # Import the time module
import datetime
ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/content/drive/My Drive/Torrent/', #Enter the Destination Path here 
    #By default Torrent File would be saved in a folder "Torrent" in selected Drive
    'storage_mode': lt.storage_mode_t(2), # Use Sparse Storage Mode
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True}
# Magnet Link Goes Here
link = "YOUR MAGNET LINK HERE"
print(link)

# Create add_torrent_params object and set the magnet link as url
params = lt.add_torrent_params()
params.save_path = '/content/drive/My Drive/Torrent/'
params.storage_mode = lt.storage_mode_t(2)
params.url = link
#params.paused = False # Start the download immediately
#params.auto_managed = True # Let libtorrent manage the download automatically

# Add the torrent to the session
handle = ses.add_torrent(params)

ses.start_dht()

begin = time.time()
print(datetime.datetime.now())

print('Downloading Metadata...')
while (not handle.has_metadata()):
    time.sleep(1)
print('MataData Imported, Attempting Download')

print("Starting, Please Wait\n", handle.name())

# Print download progress
while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
            'downloading', 'finished', 'seeding', 'allocating']
    print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % \
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
            s.num_peers, state_str[s.state]))
    time.sleep(5)

end = time.time()
print(handle.name(), "COMPLETE, Go to the Drive to Find the Downloaded File")

# Print elapsed time
print("Elapsed Time: ", int((end - begin) // 60), "min :", int((end - begin) % 60), "sec")
print("Closing Session, Come Back Again")
print(datetime.datetime.now)
