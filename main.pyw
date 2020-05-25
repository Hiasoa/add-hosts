try:
    import sys, time, os, shutil
except:
    print('import error')
    error


print('reset : type "R"\nadd : type "A"')
mode = input('mode:')



if mode == 'A':
    os.chdir('./')

    hosts = 'C:\\Windows\\System32\\drivers\\etc\\hosts'

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
if mode == 'R':
    os.system('del C:\\Windows\\System32\\drivers\\etc\\hosts')
    os.system('echo.> C:\\Windows\\System32\\drivers\\etc\\hosts')