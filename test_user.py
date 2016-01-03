import user
import package_manager


#change these to actual unit tests at some point
def test_add_package():
	mock_user = user.User()
	mock_user.add_package('test_package')
	mock_user.add_package('other')
	mock_user.add_package('final')

def test_reapfile():
    mock_user = user.User()
	manager = PackageManager(mock_user)
	manager.process_reapfile()
	input('press a key to close this window')
