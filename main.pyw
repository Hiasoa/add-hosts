try:
    import sys, time, os, shutil
except:
    print('import error')
    error


print('reset : type "reset"\nadd : type "add"\nlist : type "list"')
mode = input('mode:')

hosts = 'C:\\Windows\\System32\\drivers\\etc\\hosts'

if mode == 'add':
    os.chdir('./')

    shutil.copyfile(hosts, 'hosts')

    S_ip=input('server ip:')

    if S_ip == '':
        print('error')
        sys.exit('')

    time.sleep(0)

    f = open('hosts', 'r+')

    hosts_list=f.read().splitlines()
    hosts_list.append('127.0.0.1 ' + S_ip)
    f.write('\n'.join(hosts_list))
    f.close

    print('success!')
    time.sleep(3)
    sys.exit('')
if mode == 'reset':
    os.system('echo.> C:\\Windows\\System32\\drivers\\etc\\hosts')
    print('success!')
    time.sleep(3)
    os.exit('')
if mode == 'list':
    print(open(hosts).readline())
    time.sleep(3)
    os.exit('')
