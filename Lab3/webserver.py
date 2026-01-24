Last login: Tue Jan 20 12:03:13 on ttys000
(base) sanya@52:c4:f6:f0:eb:b3 ~ % ssh sanyapeterpi@192.168.2.99
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:UTYxsRDeHuIyn4zQ5Ln3QpFzoJQ1d4RlNyFtAbgexcw.
Please contact your system administrator.
Add correct host key in /Users/sanya/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /Users/sanya/.ssh/known_hosts:6
Host key for 192.168.2.99 has changed and you have requested strict checking.
Host key verification failed.
(base) sanya@52:c4:f6:f0:eb:b3 ~ % ssh-keygen -R 192.168.2.99
# Host 192.168.2.99 found: line 4
# Host 192.168.2.99 found: line 5
# Host 192.168.2.99 found: line 6
/Users/sanya/.ssh/known_hosts updated.
Original contents retained as /Users/sanya/.ssh/known_hosts.old
(base) sanya@52:c4:f6:f0:eb:b3 ~ % ssh sanyapeterpi@192.168.2.99
The authenticity of host '192.168.2.99 (192.168.2.99)' can't be established.
ED25519 key fingerprint is SHA256:UTYxsRDeHuIyn4zQ5Ln3QpFzoJQ1d4RlNyFtAbgexcw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.2.99' (ED25519) to the list of known hosts.
sanyapeterpi@192.168.2.99's password: 
Linux sanyapeterpi 6.12.47+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.12.47-1+rpt1 (2025-09-16) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
sanyapeterpi@sanyapeterpi:~ $ cd SYSC_3010
ls
-bash: cd: SYSC_3010: No such file or directory
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
sanyapeterpi@sanyapeterpi:~ $ mkdir lab3
cd lab3
sanyapeterpi@sanyapeterpi:~/lab3 $ pwd
/home/sanyapeterpi/lab3
sanyapeterpi@sanyapeterpi:~/lab3 $ python3 -m venv venv --system-site-packages
sanyapeterpi@sanyapeterpi:~/lab3 $ source venv/bin/activate
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ pip install --upgrade pip
pip install plotly pandas
Requirement already satisfied: pip in ./venv/lib/python3.13/site-packages (25.1.1)
Collecting pip
  Downloading pip-25.3-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-25.3-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 7.4 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.1.1
    Uninstalling pip-25.1.1:
      Successfully uninstalled pip-25.1.1
Successfully installed pip-25.3
Collecting plotly
  Downloading plotly-6.5.2-py3-none-any.whl.metadata (8.5 kB)
Collecting pandas
  Downloading pandas-3.0.0.tar.gz (4.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 8.3 MB/s  0:00:00
  Installing build dependencies ... |^canceled
ERROR: Operation cancelled by user
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ pip install --upgrade pip
pip install plotly pandas
Requirement already satisfied: pip in ./venv/lib/python3.13/site-packages (25.3)
Collecting plotly
  Using cached plotly-6.5.2-py3-none-any.whl.metadata (8.5 kB)
Collecting pandas
  Using cached pandas-3.0.0.tar.gz (4.6 MB)
  Installing build dependencies ... \^canceled
ERROR: Operation cancelled by user
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ deactivate
sanyapeterpi@sanyapeterpi:~/lab3 $ cd ~/SYSC_3010
-bash: cd: /home/sanyapeterpi/SYSC_3010: No such file or directory
sanyapeterpi@sanyapeterpi:~/lab3 $ source venv/bin/activate
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 -m pip install --upgrade pip
python3 -m pip install pyrebase4
Requirement already satisfied: pip in ./venv/lib/python3.13/site-packages (25.3)
Collecting pyrebase4
  Downloading pyrebase4-4.9.0-py3-none-any.whl.metadata (664 bytes)
Collecting requests-toolbelt>=1.0.0 (from pyrebase4)
  Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
Requirement already satisfied: requests>=2.31 in /usr/lib/python3/dist-packages (from pyrebase4) (2.32.3)
Collecting urllib3<2,>=1.21.1 (from pyrebase4)
  Downloading urllib3-1.26.20-py2.py3-none-any.whl.metadata (50 kB)
Collecting google-cloud-storage>=2.18.2 (from pyrebase4)
  Downloading google_cloud_storage-3.8.0-py3-none-any.whl.metadata (14 kB)
Collecting oauth2client>=4.1.2 (from pyrebase4)
  Downloading oauth2client-4.1.3-py2.py3-none-any.whl.metadata (1.2 kB)
Collecting python-jwt>=2.0.1 (from pyrebase4)
  Downloading python_jwt-4.1.0-py2.py3-none-any.whl.metadata (5.6 kB)
Collecting pycryptodome>=3.6.4 (from pyrebase4)
  Downloading pycryptodome-3.23.0.tar.gz (4.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 8.5 MB/s  0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting google-auth<3.0.0,>=2.26.1 (from google-cloud-storage>=2.18.2->pyrebase4)
  Downloading google_auth-2.47.0-py3-none-any.whl.metadata (6.4 kB)
Collecting google-api-core<3.0.0,>=2.27.0 (from google-cloud-storage>=2.18.2->pyrebase4)
  Downloading google_api_core-2.29.0-py3-none-any.whl.metadata (3.3 kB)
Collecting google-cloud-core<3.0.0,>=2.4.2 (from google-cloud-storage>=2.18.2->pyrebase4)
  Downloading google_cloud_core-2.5.0-py3-none-any.whl.metadata (3.1 kB)
Collecting google-resumable-media<3.0.0,>=2.7.2 (from google-cloud-storage>=2.18.2->pyrebase4)
  Downloading google_resumable_media-2.8.0-py3-none-any.whl.metadata (2.6 kB)
Collecting google-crc32c<2.0.0,>=1.1.3 (from google-cloud-storage>=2.18.2->pyrebase4)
  Downloading google_crc32c-1.8.0.tar.gz (14 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting googleapis-common-protos<2.0.0,>=1.56.2 (from google-api-core<3.0.0,>=2.27.0->google-cloud-storage>=2.18.2->pyrebase4)
  Downloading googleapis_common_protos-1.72.0-py3-none-any.whl.metadata (9.4 kB)
Collecting protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<7.0.0,>=3.19.5 (from google-api-core<3.0.0,>=2.27.0->google-cloud-storage>=2.18.2->pyrebase4)
  Downloading protobuf-6.33.4-py3-none-any.whl.metadata (593 bytes)
Collecting proto-plus<2.0.0,>=1.22.3 (from google-api-core<3.0.0,>=2.27.0->google-cloud-storage>=2.18.2->pyrebase4)
  Downloading proto_plus-1.27.0-py3-none-any.whl.metadata (2.2 kB)
Collecting pyasn1-modules>=0.2.1 (from google-auth<3.0.0,>=2.26.1->google-cloud-storage>=2.18.2->pyrebase4)
  Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
Collecting rsa<5,>=3.1.4 (from google-auth<3.0.0,>=2.26.1->google-cloud-storage>=2.18.2->pyrebase4)
  Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/lib/python3/dist-packages (from requests>=2.31->pyrebase4) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests>=2.31->pyrebase4) (3.10)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests>=2.31->pyrebase4) (2025.1.31)
Collecting pyasn1>=0.1.3 (from rsa<5,>=3.1.4->google-auth<3.0.0,>=2.26.1->google-cloud-storage>=2.18.2->pyrebase4)
  Downloading pyasn1-0.6.2-py3-none-any.whl.metadata (8.4 kB)
Collecting httplib2>=0.9.1 (from oauth2client>=4.1.2->pyrebase4)
  Downloading httplib2-0.31.2-py3-none-any.whl.metadata (2.2 kB)
Collecting six>=1.6.1 (from oauth2client>=4.1.2->pyrebase4)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting pyparsing<4,>=3.1 (from httplib2>=0.9.1->oauth2client>=4.1.2->pyrebase4)
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting jwcrypto>=1.4.2 (from python-jwt>=2.0.1->pyrebase4)
  Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
Requirement already satisfied: cryptography>=3.4 in /usr/lib/python3/dist-packages (from jwcrypto>=1.4.2->python-jwt>=2.0.1->pyrebase4) (43.0.0)
Requirement already satisfied: typing-extensions>=4.5.0 in /usr/lib/python3/dist-packages (from jwcrypto>=1.4.2->python-jwt>=2.0.1->pyrebase4) (4.13.2)
Downloading pyrebase4-4.9.0-py3-none-any.whl (9.1 kB)
Downloading urllib3-1.26.20-py2.py3-none-any.whl (144 kB)
Downloading google_cloud_storage-3.8.0-py3-none-any.whl (312 kB)
Downloading google_api_core-2.29.0-py3-none-any.whl (173 kB)
Downloading google_auth-2.47.0-py3-none-any.whl (234 kB)
Downloading google_cloud_core-2.5.0-py3-none-any.whl (29 kB)
Downloading google_resumable_media-2.8.0-py3-none-any.whl (81 kB)
Downloading googleapis_common_protos-1.72.0-py3-none-any.whl (297 kB)
Downloading proto_plus-1.27.0-py3-none-any.whl (50 kB)
Downloading protobuf-6.33.4-py3-none-any.whl (170 kB)
Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
Downloading oauth2client-4.1.3-py2.py3-none-any.whl (98 kB)
Downloading httplib2-0.31.2-py3-none-any.whl (91 kB)
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
Downloading pyasn1-0.6.2-py3-none-any.whl (83 kB)
Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
Downloading python_jwt-4.1.0-py2.py3-none-any.whl (7.1 kB)
Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Building wheels for collected packages: google-crc32c, pycryptodome
  Building wheel for google-crc32c (pyproject.toml) ... done
  Created wheel for google-crc32c: filename=google_crc32c-1.8.0-py3-none-any.whl size=13800 sha256=6c7c598a05d907d1c778367433486b52a993e3f907e7e436de99afed91ac22a3
  Stored in directory: /home/sanyapeterpi/.cache/pip/wheels/89/25/b4/ee61a450b2a7a5ffb7530ec99c683f548b7438d7251eddafa5
  Building wheel for pycryptodome (pyproject.toml) ... done
  Created wheel for pycryptodome: filename=pycryptodome-3.23.0-cp37-abi3-linux_armv7l.whl size=2072033 sha256=a7fe43b0f3b31001937e7a7c213e92880395a21f58e99cebc0ea7bad3aeee414
  Stored in directory: /home/sanyapeterpi/.cache/pip/wheels/29/eb/c7/c569c89bdc7331f61e744a1847d02798ce31bf1bd1cb13cb33
Successfully built google-crc32c pycryptodome
Installing collected packages: urllib3, six, pyparsing, pycryptodome, pyasn1, protobuf, jwcrypto, google-crc32c, rsa, python-jwt, pyasn1-modules, proto-plus, httplib2, googleapis-common-protos, google-resumable-media, requests-toolbelt, oauth2client, google-auth, google-api-core, google-cloud-core, google-cloud-storage, pyrebase4
  Attempting uninstall: urllib3
    Found existing installation: urllib3 2.3.0
    Not uninstalling urllib3 at /usr/lib/python3/dist-packages, outside environment /home/sanyapeterpi/lab3/venv
    Can't uninstall 'urllib3'. No files were found to uninstall.
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
types-requests 2.32 requires urllib3>=2, but you have urllib3 1.26.20 which is incompatible.
types-influxdb-client 1.45 requires urllib3>=2, but you have urllib3 1.26.20 which is incompatible.
types-docker 7.1 requires urllib3>=2, but you have urllib3 1.26.20 which is incompatible.
Successfully installed google-api-core-2.29.0 google-auth-2.47.0 google-cloud-core-2.5.0 google-cloud-storage-3.8.0 google-crc32c-1.8.0 google-resumable-media-2.8.0 googleapis-common-protos-1.72.0 httplib2-0.31.2 jwcrypto-1.5.6 oauth2client-4.1.3 proto-plus-1.27.0 protobuf-6.33.4 pyasn1-0.6.2 pyasn1-modules-0.4.2 pycryptodome-3.23.0 pyparsing-3.3.2 pyrebase4-4.9.0 python-jwt-4.1.0 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 urllib3-1.26.20
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ cd ~/lab3
wget https://raw.githubusercontent.com/CU-SYSC3010W25/SYSC3010-W25-Files/main/firebase-snippets.py
--2026-01-23 14:58:03--  https://raw.githubusercontent.com/CU-SYSC3010W25/SYSC3010-W25-Files/main/firebase-snippets.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2026-01-23 14:58:04 ERROR 404: Not Found.

(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano firebase-snippets.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ pip install Flask
Requirement already satisfied: Flask in /usr/lib/python3/dist-packages (3.1.1)
Requirement already satisfied: blinker>=1.9.0 in /usr/lib/python3/dist-packages (from Flask) (1.9.0)
Requirement already satisfied: click>=8.1.3 in /usr/lib/python3/dist-packages (from Flask) (8.1.8)
Requirement already satisfied: itsdangerous>=2.2.0 in /usr/lib/python3/dist-packages (from Flask) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in /usr/lib/python3/dist-packages (from Flask) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in /usr/lib/python3/dist-packages (from Flask) (2.1.5)
Requirement already satisfied: werkzeug>=3.1.0 in /usr/lib/python3/dist-packages (from Flask) (3.1.3)
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano myflaskwebserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ mkdir templates
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano templates/hello.html
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ sudo python myflaskwebserver.py
 * Serving Flask app 'myflaskwebserver'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.2.99:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 117-178-620
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ sudo python myflaskwebserver.py
 * Serving Flask app 'myflaskwebserver'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.2.99:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 117-178-620
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ sudo python myflaskwebserver.py
 * Serving Flask app 'myflaskwebserver'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.2.99:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 117-178-620
192.168.2.99 - - [23/Jan/2026 15:56:29] "GET / HTTP/1.1" 200 -
192.168.2.99 - - [23/Jan/2026 15:56:29] "GET /favicon.ico HTTP/1.1" 404 -
192.168.2.99 - - [23/Jan/2026 15:57:28] "GET /hello HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1536, in __call__
    return self.wsgi_app(environ, start_response)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/sanyapeterpi/lab3/myflaskwebserver.py", line 12, in hello_name
    return render_template("hello.html", name=name)
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
192.168.2.99 - - [23/Jan/2026 15:57:28] "GET /hello?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
192.168.2.99 - - [23/Jan/2026 15:57:28] "GET /hello?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
192.168.2.99 - - [23/Jan/2026 15:57:29] "GET /hello?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
192.168.2.99 - - [23/Jan/2026 15:57:38] "GET /hello HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1536, in __call__
    return self.wsgi_app(environ, start_response)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/sanyapeterpi/lab3/myflaskwebserver.py", line 12, in hello_name
    return render_template("hello.html", name=name)
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
192.168.2.99 - - [23/Jan/2026 15:57:38] "GET /hello?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
192.168.2.99 - - [23/Jan/2026 15:57:38] "GET /hello?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
192.168.2.99 - - [23/Jan/2026 15:57:38] "GET /hello?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
192.168.2.99 - - [23/Jan/2026 15:57:42] "GET / HTTP/1.1" 200 -
192.168.2.99 - - [23/Jan/2026 15:58:28] "GET /hello HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1536, in __call__
    return self.wsgi_app(environ, start_response)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/sanyapeterpi/lab3/myflaskwebserver.py", line 12, in hello_name
    return render_template("hello.html", name=name)
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
192.168.2.99 - - [23/Jan/2026 15:58:28] "GET /hello?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 -
192.168.2.99 - - [23/Jan/2026 15:58:28] "GET /hello?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 -
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 cd ~/lab3b3
pwd
/home/sanyapeterpi/lab3
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ls -l myflaskwebserver.py
-rw-rw-r-- 1 sanyapeterpi sanyapeterpi 301 Jan 23 15:41 myflaskwebserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ls -l templates
total 4
-rw-rw-r-- 1 sanyapeterpi sanyapeterpi 121 Jan 23 15:42 hello.html
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ cat templates/hello.html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello {{ name }}</h1>
</body>
</html>
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ sudo python myflaskwebserver.py
 * Serving Flask app 'myflaskwebserver'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.2.99:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 117-178-620
192.168.2.99 - - [23/Jan/2026 16:00:15] "GET /hello HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1536, in __call__
    return self.wsgi_app(environ, start_response)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/sanyapeterpi/lab3/myflaskwebserver.py", line 12, in hello_name
    return render_template("hello.html", name=name)
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
192.168.2.99 - - [23/Jan/2026 16:00:16] "GET /hello?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 -
192.168.2.99 - - [23/Jan/2026 16:00:16] "GET /hello?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 -
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 nano ~/lab3/myflaskwebserver.pypy
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ sudo python myflaskwebserver.py
 * Serving Flask app 'myflaskwebserver'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.2.99:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 117-178-620
192.168.2.99 - - [23/Jan/2026 16:01:59] "GET /hello HTTP/1.1" 200 -
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ cat templates/hello.html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello {{ name }}</h1>
</body>
</html>
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ pip install flask-socketio
pip install eventlet
Collecting flask-socketio
  Downloading flask_socketio-5.6.0-py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: Flask>=2.1.0 in /usr/lib/python3/dist-packages (from flask-socketio) (3.1.1)
Collecting python-socketio>=5.12.0 (from flask-socketio)
  Downloading python_socketio-5.16.0-py3-none-any.whl.metadata (3.2 kB)
Requirement already satisfied: blinker>=1.9.0 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (1.9.0)
Requirement already satisfied: click>=8.1.3 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (8.1.8)
Requirement already satisfied: itsdangerous>=2.2.0 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (2.1.5)
Requirement already satisfied: werkzeug>=3.1.0 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (3.1.3)
Collecting bidict>=0.21.0 (from python-socketio>=5.12.0->flask-socketio)
  Downloading bidict-0.23.1-py3-none-any.whl.metadata (8.7 kB)
Collecting python-engineio>=4.11.0 (from python-socketio>=5.12.0->flask-socketio)
  Downloading python_engineio-4.13.0-py3-none-any.whl.metadata (2.3 kB)
Collecting simple-websocket>=0.10.0 (from python-engineio>=4.11.0->python-socketio>=5.12.0->flask-socketio)
  Downloading simple_websocket-1.1.0-py3-none-any.whl.metadata (1.5 kB)
Collecting wsproto (from simple-websocket>=0.10.0->python-engineio>=4.11.0->python-socketio>=5.12.0->flask-socketio)
  Downloading wsproto-1.3.2-py3-none-any.whl.metadata (5.2 kB)
Collecting h11<1,>=0.16.0 (from wsproto->simple-websocket>=0.10.0->python-engineio>=4.11.0->python-socketio>=5.12.0->flask-socketio)
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Downloading flask_socketio-5.6.0-py3-none-any.whl (18 kB)
Downloading python_socketio-5.16.0-py3-none-any.whl (79 kB)
Downloading bidict-0.23.1-py3-none-any.whl (32 kB)
Downloading python_engineio-4.13.0-py3-none-any.whl (59 kB)
Downloading simple_websocket-1.1.0-py3-none-any.whl (13 kB)
Downloading wsproto-1.3.2-py3-none-any.whl (24 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Installing collected packages: h11, bidict, wsproto, simple-websocket, python-engineio, python-socketio, flask-socketio
Successfully installed bidict-0.23.1 flask-socketio-5.6.0 h11-0.16.0 python-engineio-4.13.0 python-socketio-5.16.0 simple-websocket-1.1.0 wsproto-1.3.2
Collecting eventlet
  Downloading eventlet-0.40.4-py3-none-any.whl.metadata (5.5 kB)
Collecting dnspython>=1.15.0 (from eventlet)
  Downloading dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
Collecting greenlet>=1.0 (from eventlet)
  Downloading greenlet-3.3.1.tar.gz (184 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Downloading eventlet-0.40.4-py3-none-any.whl (364 kB)
Downloading dnspython-2.8.0-py3-none-any.whl (331 kB)
Building wheels for collected packages: greenlet
  Building wheel for greenlet (pyproject.toml) ... done
  Created wheel for greenlet: filename=greenlet-3.3.1-cp313-cp313-linux_armv7l.whl size=534556 sha256=5d1cfa14dfab27cd98aea7c4151a408678ce0ebf582cdad32b73c3568176f863
  Stored in directory: /home/sanyapeterpi/.cache/pip/wheels/f7/a2/a2/2c9cb63e4c3c50a4d524dda82c52c6e3ce280932c3af1c0cf6
Successfully built greenlet
Installing collected packages: greenlet, dnspython, eventlet
Successfully installed dnspython-2.8.0 eventlet-0.40.4 greenlet-3.3.1
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ pip install flask
pip install flask-socketio
pip install eventlet
pip install sense-hat
Requirement already satisfied: flask in /usr/lib/python3/dist-packages (3.1.1)
Requirement already satisfied: blinker>=1.9.0 in /usr/lib/python3/dist-packages (from flask) (1.9.0)
Requirement already satisfied: click>=8.1.3 in /usr/lib/python3/dist-packages (from flask) (8.1.8)
Requirement already satisfied: itsdangerous>=2.2.0 in /usr/lib/python3/dist-packages (from flask) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in /usr/lib/python3/dist-packages (from flask) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in /usr/lib/python3/dist-packages (from flask) (2.1.5)
Requirement already satisfied: werkzeug>=3.1.0 in /usr/lib/python3/dist-packages (from flask) (3.1.3)
Requirement already satisfied: flask-socketio in ./venv/lib/python3.13/site-packages (5.6.0)
Requirement already satisfied: Flask>=2.1.0 in /usr/lib/python3/dist-packages (from flask-socketio) (3.1.1)
Requirement already satisfied: python-socketio>=5.12.0 in ./venv/lib/python3.13/site-packages (from flask-socketio) (5.16.0)
Requirement already satisfied: blinker>=1.9.0 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (1.9.0)
Requirement already satisfied: click>=8.1.3 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (8.1.8)
Requirement already satisfied: itsdangerous>=2.2.0 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (2.1.5)
Requirement already satisfied: werkzeug>=3.1.0 in /usr/lib/python3/dist-packages (from Flask>=2.1.0->flask-socketio) (3.1.3)
Requirement already satisfied: bidict>=0.21.0 in ./venv/lib/python3.13/site-packages (from python-socketio>=5.12.0->flask-socketio) (0.23.1)
Requirement already satisfied: python-engineio>=4.11.0 in ./venv/lib/python3.13/site-packages (from python-socketio>=5.12.0->flask-socketio) (4.13.0)
Requirement already satisfied: simple-websocket>=0.10.0 in ./venv/lib/python3.13/site-packages (from python-engineio>=4.11.0->python-socketio>=5.12.0->flask-socketio) (1.1.0)
Requirement already satisfied: wsproto in ./venv/lib/python3.13/site-packages (from simple-websocket>=0.10.0->python-engineio>=4.11.0->python-socketio>=5.12.0->flask-socketio) (1.3.2)
Requirement already satisfied: h11<1,>=0.16.0 in ./venv/lib/python3.13/site-packages (from wsproto->simple-websocket>=0.10.0->python-engineio>=4.11.0->python-socketio>=5.12.0->flask-socketio) (0.16.0)
Requirement already satisfied: eventlet in ./venv/lib/python3.13/site-packages (0.40.4)
Requirement already satisfied: dnspython>=1.15.0 in ./venv/lib/python3.13/site-packages (from eventlet) (2.8.0)
Requirement already satisfied: greenlet>=1.0 in ./venv/lib/python3.13/site-packages (from eventlet) (3.3.1)
Requirement already satisfied: sense-hat in /usr/lib/python3/dist-packages (2.6.0)
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano templates/Lab3-Colour-Picker.htm
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ls -l
ls -l templates
total 16
-rw-rw-r-- 1 sanyapeterpi sanyapeterpi  319 Jan 23 16:01 myflaskwebserver.py
drwxrwxr-x 2 sanyapeterpi sanyapeterpi 4096 Jan 23 16:56 templates
drwxrwxr-x 6 sanyapeterpi sanyapeterpi 4096 Jan 23 14:46 venv
-rw-rw-r-- 1 sanyapeterpi sanyapeterpi 2888 Jan 23 16:55 webserver.py
total 8
-rw-rw-r-- 1 sanyapeterpi sanyapeterpi  121 Jan 23 15:42 hello.html
-rw-rw-r-- 1 sanyapeterpi sanyapeterpi 3443 Jan 23 16:56 Lab3-Colour-Picker.htm
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6810) wsgi starting up on http://0.0.0.0:5000
(6810) accepted ('192.168.2.99', 43476)
192.168.2.99 - - [23/Jan/2026 16:57:05] "GET /hello HTTP/1.1" 404 355 0.002843
(6810) accepted ('192.168.2.99', 43488)
(6810) accepted ('192.168.2.99', 35802)
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/sanyapeterpi/lab3/webserver.py", line 34, in index
    return render_template('Lab3-Colour-Picker.html')
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 149, in render_template
    template = app.jinja_env.get_or_select_template(template_name_or_list)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1087, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1016, in get_template
    return self._load_template(name, globals)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 975, in _load_template
    template = self.loader.load(self, name, self.make_globals(globals))
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 126, in load
    source, filename, uptodate = self.get_source(environment, name)
                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 65, in get_source
    return self._get_source_fast(environment, template)
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 99, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: Lab3-Colour-Picker.html
192.168.2.99 - - [23/Jan/2026 17:02:28] "GET / HTTP/1.1" 500 24993 0.057676
(6810) accepted ('192.168.2.99', 35814)
192.168.2.99 - - [23/Jan/2026 17:02:28] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 6312 0.017255
192.168.2.99 - - [23/Jan/2026 17:02:28] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 10311 0.001761
192.168.2.99 - - [23/Jan/2026 17:02:28] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 729 0.001259
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ 
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6818) wsgi starting up on http://0.0.0.0:5000
(6818) accepted ('192.168.2.99', 51314)
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/sanyapeterpi/lab3/webserver.py", line 34, in index
    return render_template('Lab3-Colour-Picker.html')
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 149, in render_template
    template = app.jinja_env.get_or_select_template(template_name_or_list)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1087, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1016, in get_template
    return self._load_template(name, globals)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 975, in _load_template
    template = self.loader.load(self, name, self.make_globals(globals))
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 126, in load
    source, filename, uptodate = self.get_source(environment, name)
                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 65, in get_source
    return self._get_source_fast(environment, template)
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 99, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: Lab3-Colour-Picker.html
192.168.2.99 - - [23/Jan/2026 17:02:47] "GET / HTTP/1.1" 500 24993 0.046585
(6818) accepted ('192.168.2.99', 51324)
192.168.2.99 - - [23/Jan/2026 17:02:47] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 183 0.021094
192.168.2.99 - - [23/Jan/2026 17:02:47] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 184 0.002408
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ 
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ 
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ cd ~/lab3
python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6848) wsgi starting up on http://0.0.0.0:5000
(6848) accepted ('192.168.2.99', 35578)
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/sanyapeterpi/lab3/webserver.py", line 34, in index
    return render_template('Lab3-Colour-Picker.html')
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 149, in render_template
    template = app.jinja_env.get_or_select_template(template_name_or_list)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1087, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1016, in get_template
    return self._load_template(name, globals)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 975, in _load_template
    template = self.loader.load(self, name, self.make_globals(globals))
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 126, in load
    source, filename, uptodate = self.get_source(environment, name)
                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 65, in get_source
    return self._get_source_fast(environment, template)
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 99, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: Lab3-Colour-Picker.html
192.168.2.99 - - [23/Jan/2026 17:05:07] "GET / HTTP/1.1" 500 24993 0.042333
(6848) accepted ('192.168.2.99', 35594)
192.168.2.99 - - [23/Jan/2026 17:05:07] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 184 0.022855
192.168.2.99 - - [23/Jan/2026 17:05:07] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 183 0.001657
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ^[[200~ls templates/
-bash: $'\E[200~ls': command not found
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ~ls templates/
-bash: ~ls: command not found
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ls templates/
hello.html  Lab3-Colour-Picker.htm
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6856) wsgi starting up on http://0.0.0.0:5000
(6856) accepted ('192.168.2.99', 38384)
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/sanyapeterpi/lab3/webserver.py", line 34, in index
    return render_template('Lab3-Colour-Picker.html')
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 149, in render_template
    template = app.jinja_env.get_or_select_template(template_name_or_list)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1087, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1016, in get_template
    return self._load_template(name, globals)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 975, in _load_template
    template = self.loader.load(self, name, self.make_globals(globals))
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 126, in load
    source, filename, uptodate = self.get_source(environment, name)
                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 65, in get_source
    return self._get_source_fast(environment, template)
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 99, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: Lab3-Colour-Picker.html
192.168.2.99 - - [23/Jan/2026 17:06:18] "GET / HTTP/1.1" 500 24993 0.046289
(6856) accepted ('192.168.2.99', 38388)
192.168.2.99 - - [23/Jan/2026 17:06:18] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 183 0.024124
192.168.2.99 - - [23/Jan/2026 17:06:18] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 184 0.002499
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ 
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ls
myflaskwebserver.py  templates  venv  webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ls -l
total 16
-rw-rw-r-- 1 sanyapeterpi sanyapeterpi  319 Jan 23 16:01 myflaskwebserver.py
drwxrwxr-x 2 sanyapeterpi sanyapeterpi 4096 Jan 23 16:56 templates
drwxrwxr-x 6 sanyapeterpi sanyapeterpi 4096 Jan 23 14:46 venv
-rw-rw-r-- 1 sanyapeterpi sanyapeterpi 2888 Jan 23 16:55 webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ls templates/
hello.html  Lab3-Colour-Picker.htm
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ ls templates/
hello.html  Lab3-Colour-Picker.html
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6894) wsgi starting up on http://0.0.0.0:5000
(6894) accepted ('192.168.2.99', 55568)
192.168.2.99 - - [23/Jan/2026 17:07:33] "GET / HTTP/1.1" 200 3584 0.009316
(6894) accepted ('192.168.2.99', 55582)
192.168.2.99 - - [23/Jan/2026 17:07:33] "GET /socket.io/?EIO=4&transport=polling&t=PlivVcT HTTP/1.1" 200 300 0.002389
sending colors.. {"colors": [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]}
192.168.2.99 - - [23/Jan/2026 17:07:33] "POST /socket.io/?EIO=4&transport=polling&t=PlivVc-&sid=oCp5NyfBAer1aq9CAAAA HTTP/1.1" 200 222 0.007821
(6894) accepted ('192.168.2.99', 55584)
192.168.2.99 - - [23/Jan/2026 17:07:33] "GET /socket.io/?EIO=4&transport=polling&t=PlivVd-&sid=oCp5NyfBAer1aq9CAAAA HTTP/1.1" 200 1148 0.001856
192.168.2.99 - - [23/Jan/2026 17:07:33] "GET /socket.io/?EIO=4&transport=polling&t=PlivVeh&sid=oCp5NyfBAer1aq9CAAAA HTTP/1.1" 200 181 0.000787
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ 
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6921) wsgi starting up on http://0.0.0.0:5000
(6921) accepted ('192.168.2.99', 53438)
192.168.2.99 - - [23/Jan/2026 17:13:48] "GET / HTTP/1.1" 200 3584 0.010597
(6921) accepted ('192.168.2.99', 53450)
192.168.2.99 - - [23/Jan/2026 17:13:49] "GET /socket.io/?EIO=4&transport=polling&t=PliwxK_ HTTP/1.1" 200 300 0.002131
sending colors.. {"colors": [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]}
192.168.2.99 - - [23/Jan/2026 17:13:49] "POST /socket.io/?EIO=4&transport=polling&t=PliwxLb&sid=h-OK-TDJMhpbsR4sAAAA HTTP/1.1" 200 222 0.008893
192.168.2.99 - - [23/Jan/2026 17:13:49] "GET /socket.io/?EIO=4&transport=polling&t=PliwxLm&sid=h-OK-TDJMhpbsR4sAAAA HTTP/1.1" 200 1148 0.000614
(6921) accepted ('192.168.2.99', 53454)
192.168.2.99 - - [23/Jan/2026 17:13:49] "GET /socket.io/?EIO=4&transport=polling&t=PliwxMC&sid=h-OK-TDJMhpbsR4sAAAA HTTP/1.1" 200 181 0.001108
192.168.2.99 - - [23/Jan/2026 17:13:49] "GET /socket.io/?EIO=4&transport=polling&t=PliwxMj&sid=h-OK-TDJMhpbsR4sAAAA HTTP/1.1" 200 181 0.000536
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano templates/Lab3-Colour-Picker.htm
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6930) wsgi starting up on http://0.0.0.0:5000
(6930) accepted ('192.168.2.99', 45092)
192.168.2.99 - - [23/Jan/2026 17:15:12] "GET / HTTP/1.1" 200 3584 0.013738
(6930) accepted ('192.168.2.99', 45096)
192.168.2.99 - - [23/Jan/2026 17:15:13] "GET /socket.io/?EIO=4&transport=polling&t=PlixFsN HTTP/1.1" 200 300 0.001264
sending colors.. {"colors": [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]}
192.168.2.99 - - [23/Jan/2026 17:15:13] "POST /socket.io/?EIO=4&transport=polling&t=PlixFt0&sid=BB8KrIrv9nn4hI3cAAAA HTTP/1.1" 200 222 0.005988
(6930) accepted ('192.168.2.99', 45106)
192.168.2.99 - - [23/Jan/2026 17:15:13] "GET /socket.io/?EIO=4&transport=polling&t=PlixFtC&sid=BB8KrIrv9nn4hI3cAAAA HTTP/1.1" 200 1148 0.000710
192.168.2.99 - - [23/Jan/2026 17:15:13] "GET /socket.io/?EIO=4&transport=polling&t=PlixFta&sid=BB8KrIrv9nn4hI3cAAAA HTTP/1.1" 200 181 0.000607
192.168.2.99 - - [23/Jan/2026 17:16:00] "GET /socket.io/?EIO=4&transport=websocket&sid=BB8KrIrv9nn4hI3cAAAA HTTP/1.1" 200 0 47.886371
192.168.2.99 - - [23/Jan/2026 17:16:01] "GET / HTTP/1.1" 200 3584 0.002640
192.168.2.99 - - [23/Jan/2026 17:16:01] "GET /socket.io/?EIO=4&transport=polling&t=PlixRbW HTTP/1.1" 200 300 0.000720
sending colors.. {"colors": [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]}
192.168.2.99 - - [23/Jan/2026 17:16:01] "POST /socket.io/?EIO=4&transport=polling&t=PlixRb_&sid=-Yr-8ZXDK3B-U00wAAAC HTTP/1.1" 200 222 0.005437
192.168.2.99 - - [23/Jan/2026 17:16:01] "GET /socket.io/?EIO=4&transport=polling&t=PlixRc3&sid=-Yr-8ZXDK3B-U00wAAAC HTTP/1.1" 200 956 0.000545
(6930) accepted ('192.168.2.99', 46380)
192.168.2.99 - - [23/Jan/2026 17:16:01] "GET /socket.io/?EIO=4&transport=polling&t=PlixRcK&sid=-Yr-8ZXDK3B-U00wAAAC HTTP/1.1" 200 181 0.001325
192.168.2.99 - - [23/Jan/2026 17:16:01] "GET /socket.io/?EIO=4&transport=polling&t=PlixRcY&sid=-Yr-8ZXDK3B-U00wAAAC HTTP/1.1" 200 181 0.000488
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ 
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano templates/Lab3-Colour-Picker.htm
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6965) wsgi starting up on http://0.0.0.0:5000
(6965) accepted ('192.168.2.99', 60702)
192.168.2.99 - - [23/Jan/2026 17:33:59] "GET / HTTP/1.1" 200 3584 0.011315
(6965) accepted ('192.168.2.99', 60704)
192.168.2.99 - - [23/Jan/2026 17:33:59] "GET /socket.io/?EIO=4&transport=polling&t=Pli_YvU HTTP/1.1" 200 300 0.001008
sending colors.. {"colors": [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]}
192.168.2.99 - - [23/Jan/2026 17:33:59] "POST /socket.io/?EIO=4&transport=polling&t=Pli_Yw0&sid=QoL24DkSxyP0Md-oAAAA HTTP/1.1" 200 222 0.007113
192.168.2.99 - - [23/Jan/2026 17:33:59] "GET /socket.io/?EIO=4&transport=polling&t=Pli_Yw4&sid=QoL24DkSxyP0Md-oAAAA HTTP/1.1" 200 1148 0.001147
(6965) accepted ('192.168.2.99', 60716)
192.168.2.99 - - [23/Jan/2026 17:33:59] "GET /socket.io/?EIO=4&transport=polling&t=Pli_YwO&sid=QoL24DkSxyP0Md-oAAAA HTTP/1.1" 200 181 0.000548
192.168.2.99 - - [23/Jan/2026 17:34:13] "GET /socket.io/?EIO=4&transport=websocket&sid=QoL24DkSxyP0Md-oAAAA HTTP/1.1" 200 0 13.973181
192.168.2.99 - - [23/Jan/2026 17:34:13] "GET / HTTP/1.1" 200 3584 0.001797
192.168.2.99 - - [23/Jan/2026 17:34:13] "GET /socket.io/?EIO=4&transport=polling&t=Pli_cMJ HTTP/1.1" 200 300 0.001305
sending colors.. {"colors": [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]}
192.168.2.99 - - [23/Jan/2026 17:34:13] "POST /socket.io/?EIO=4&transport=polling&t=Pli_cMW&sid=OYaaC-LpmEiPMQ2mAAAC HTTP/1.1" 200 222 0.004771
192.168.2.99 - - [23/Jan/2026 17:34:13] "GET /socket.io/?EIO=4&transport=polling&t=Pli_cMe&sid=OYaaC-LpmEiPMQ2mAAAC HTTP/1.1" 200 956 0.000484
(6965) accepted ('192.168.2.99', 45102)
192.168.2.99 - - [23/Jan/2026 17:34:13] "GET /socket.io/?EIO=4&transport=polling&t=Pli_cNF&sid=OYaaC-LpmEiPMQ2mAAAC HTTP/1.1" 200 181 0.000516
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py
(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ python3 webserver.py
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 631-015-554
(6983) wsgi starting up on http://0.0.0.0:5000
(6983) accepted ('192.168.2.99', 42164)
192.168.2.99 - - [23/Jan/2026 17:40:09] "GET /socket.io/?EIO=4&transport=polling&t=Plj0zGy HTTP/1.1" 200 300 0.000855
sending colors.. {"colors": [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]}
192.168.2.99 - - [23/Jan/2026 17:40:09] "POST /socket.io/?EIO=4&transport=polling&t=Plj0zH5&sid=M3gBYarBPQZInU0KAAAA HTTP/1.1" 200 222 0.004027
(6983) accepted ('192.168.2.99', 42172)
(6983) accepted ('192.168.2.99', 42182)
192.168.2.99 - - [23/Jan/2026 17:40:09] "GET /socket.io/?EIO=4&transport=polling&t=Plj0zH8&sid=M3gBYarBPQZInU0KAAAA HTTP/1.1" 200 1148 0.000598
192.168.2.99 - - [23/Jan/2026 17:40:09] "GET /socket.io/?EIO=4&transport=polling&t=Plj0zHM&sid=M3gBYarBPQZInU0KAAAA HTTP/1.1" 200 181 0.000422
192.168.2.99 - - [23/Jan/2026 17:40:09] "GET /socket.io/?EIO=4&transport=polling&t=Plj0zHb&sid=M3gBYarBPQZInU0KAAAA HTTP/1.1" 200 181 0.000377
192.168.2.99 - - [23/Jan/2026 17:40:10] "GET /socket.io/?EIO=4&transport=websocket&sid=M3gBYarBPQZInU0KAAAA HTTP/1.1" 200 0 0.193348
192.168.2.99 - - [23/Jan/2026 17:40:10] "GET / HTTP/1.1" 200 3584 0.008553
192.168.2.99 - - [23/Jan/2026 17:40:10] "GET /socket.io/?EIO=4&transport=polling&t=Plj0zM6 HTTP/1.1" 200 300 0.000829
sending colors.. {"colors": [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]}
192.168.2.99 - - [23/Jan/2026 17:40:10] "POST /socket.io/?EIO=4&transport=polling&t=Plj0zMi&sid=5zVoXFXR4zrlpD1GAAAC HTTP/1.1" 200 222 0.006824
(6983) accepted ('192.168.2.99', 42184)
192.168.2.99 - - [23/Jan/2026 17:40:10] "GET /socket.io/?EIO=4&transport=polling&t=Plj0zMm&sid=5zVoXFXR4zrlpD1GAAAC HTTP/1.1" 200 1148 0.000617
192.168.2.99 - - [23/Jan/2026 17:40:10] "GET /socket.io/?EIO=4&transport=polling&t=Plj0zNC&sid=5zVoXFXR4zrlpD1GAAAC HTTP/1.1" 200 181 0.001006
192.168.2.99 - - [23/Jan/2026 17:40:10] "GET /socket.io/?EIO=4&transport=polling&t=Plj0zNb&sid=5zVoXFXR4zrlpD1GAAAC HTTP/1.1" 200 181 0.000460
^C(venv) sanyapeterpi@sanyapeterpi:~/lab3 $ nano webserver.py

  GNU nano 8.4                      webserver.py                                
# and the color of set in the <colorpicker>.
# Once the color is set, the server sends a broadcast message to all
# connected clients, which updates the LED color at each webbrowser screen. 
@socketio.on('update_led')
def update_led_color(data):
    data = json.loads(data)
    color_rgb = hex_to_rgb_color(data['color'])
    colors[int(data['id'])] = color_rgb
    # Sends broadcast message to connected users.
    emit('update_led',
         json.dumps(dict(
            id=data['id'],
            color=data['color'])),
         broadcast=True)
    # Update the physical SenseHAT LEDs
    update_sensehat_leds()

#Called when a client clicks on a LED div in the web GUI.
#Updates both the server-side color array and SenseHAT LEDs.
#Broadcasts the change to all connected clients
@socketio.on('clear_leds')
def clear_leds():
    # Reset colors array
    for i in range(64):
        colors[i] = [0,0,0]
    # Update SenseHAT LEDs
    update_sensehat_leds()
    # Broadcast to all clients to update the webpage LEDs
    emit('current_colors', json.dumps(dict(colors=colors)), broadcast=True)


if __name__ == '__main__':
    # Run the Flask app with SocketIO support
    # host="0.0.0.0" allows access from other devices in the network
    socketio.run(app, host="0.0.0.0", debug=True)