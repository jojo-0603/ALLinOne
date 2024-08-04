import dns.resolver as resolver

def SubDom():
 subdomains = [
       'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 'ns2',
       'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test', 'ns', 'blog', 'pop3',
       'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns3', 'mail2', 'new', 'mysql', 'old',
       'lists', 'support', 'mobile', 'mx', 'static', 'docs', 'beta', 'shop', 'sql', 'secure',
       'demo', 'cp', 'calendar', 'wiki', 'web', 'media', 'email', 'images', 'img', 'www1',
       'intranet', 'portal', 'video', 'sip', 'dns2', 'api', 'cdn', 'stats', 'dns1', 'ns4', 'www3',
       'dns', 'search', 'staging', 'server', 'mx1', 'chat', 'wap', 'my', 'svn', 'mail1', 'sites',
       'proxy', 'ads', 'host', 'crm', 'cms', 'backup', 'mx2', 'lyncdiscover', 'info', 'apps',
       'download', 'remote', 'db', 'forums', 'store', 'relay', 'files', 'newsletter', 'app',
       'live', 'owa', 'en', 'start', 'sms', 'office', 'exchange', 'ipv4', 'mail3', 'help',
       'blogs', 'helpdesk', 'web1', 'home', 'library', 'ftp2', 'ntp', 'monitor', 'login',
       'service', 'correo', 'www4', 'moodle', 'it', 'gateway', 'gw', 'i', 'stat', 'stage', 'ldap',
       'tv', 'ssl', 'web2', 'ns5', 'upload', 'nagios', 'smtp2', 'online', 'ad', 'survey', 'data',
       'radio', 'extranet', 'test2', 'mssql', 'dns3', 'jobs', 'services', 'panel', 'irc',
       'hosting', 'cloud', 'de', 'gmail', 's', 'bbs', 'cs', 'ww', 'mrtg', 'git', 'image',
       'members', 'poczta', 's1', 'meet', 'preview', 'fr', 'cloudflare-resolve-to', 'dev2',
       'photo', 'jabber', 'legacy', 'go', 'es', 'ssh', 'redmine', 'partner', 'vps', 'server1',
       'sv', 'ns6', 'webmail2', 'av', 'community', 'cacti', 'time', 'sftp', 'lib', 'facebook',
       'www5', 'smtp1', 'feeds', 'w', 'games', 'ts', 'alumni', 'dl', 's2', 'phpmyadmin', 'archive',
       'cn', 'tools', 'stream', 'projects', 'elearning', 'im', 'iphone', 'control', 'voip',
       'test1', 'ws', 'rss', 'sp', 'wwww', 'vpn2', 'jira', 'list', 'connect', 'gallery', 'billing',
       'mailer', 'update', 'pda', 'game', 'ns0', 'testing', 'sandbox', 'job', 'events', 'dialin',
       'ml', 'fb', 'videos', 'music', 'a', 'partners', 'mailhost', 'downloads', 'reports', 'ca',
       'router', 'speedtest', 'local', 'training', 'edu', 'bugs', 'manage', 's3', 'status',
       'host2', 'ww2', 'marketing', 'conference', 'content', 'network-ip', 'broadcast-ip',
       'english', 'catalog', 'msoid', 'mailadmin', 'pay', 'access', 'streaming', 'project', 't',
       'sso', 'alpha', 'photos', 'staff', 'e', 'auth', 'v2', 'web5', 'web3', 'mail4', 'devel',
       'post', 'us', 'images2', 'master', 'rt', 'ftp1', 'qa', 'wp', 'dns4', 'www6', 'ru', 'student',
       'w3', 'citrix', 'trac', 'doc', 'img2', 'css', 'mx3', 'adm', 'web4', 'hr', 'mailserver',
       'travel', 'sharepoint', 'sport', 'member', 'bb', 'agenda', 'link', 'server2', 'vod', 'uk',
       'fw', 'promo', 'vip', 'noc', 'design', 'temp', 'gate', 'ns7', 'file', 'ms', 'map', 'cache',
       'painel', 'js', 'event', 'mailing', 'db1', 'c', 'auto', 'img1', 'vpn1', 'business', 'mirror',
       'share', 'cdn2', 'site', 'maps', 'tickets', 'tracker', 'domains', 'club', 'images1',
       'zimbra', 'cvs', 'b2b', 'oa', 'intra', 'zabbix', 'ns8', 'assets', 'main', 'spam', 'lms',
       'social', 'faq', 'feedback', 'loopback', 'groups', 'm2', 'cas', 'loghost', 'xml', 'nl',
       'research', 'art', 'munin', 'dev1', 'gis', 'sales', 'images3', 'report', 'google', 'idp',
       'cisco', 'careers', 'seo', 'dc', 'lab', 'd', 'firewall', 'fs', 'eng', 'ann', 'mail01',
       'mantis', 'v', 'affiliates', 'webconf', 'track', 'ticket', 'pm', 'db2', 'b', 'clients',
       'tech', 'erp', 'monitoring', 'cdn1', 'images4', 'payment', 'origin', 'client', 'foto',
       'domain', 'pt', 'pma', 'directory', 'cc', 'public', 'finance', 'ns11', 'test3', 'wordpress',
       'corp', 'sslvpn', 'cal', 'mailman', 'book', 'ip', 'zeus', 'ns10', 'hermes', 'storage',
       'free', 'static1', 'pbx', 'banner', 'mobil', 'kb', 'mail5', 'direct', 'ipfixe', 'wifi',
       'development', 'board', 'ns01', 'st', 'reviews', 'radius', 'pro', 'atlas', 'links', 'in',
       'oldmail', 'register', 's4', 'images6', 'static2', 'id', 'shopping', 'drupal', 'analytics',
       'm1', 'images5', 'images7', 'img3', 'mx01', 'www7', 'redirect', 'sitebuilder', 'smtp3',
       'adserver', 'net', 'user', 'forms', 'outlook', 'press', 'vc', 'health', 'work', 'mb', 'mm',
       'f', 'pgsql', 'jp', 'sports', 'preprod', 'g', 'p', 'mdm', 'ar', 'lync', 'market', 'dbadmin',
       'barracuda', 'affiliate', 'mars', 'users', 'images8', 'biblioteca', 'mc', 'ns12', 'math',
       'ntp1', 'web01', 'software', 'pr', 'jupiter', 'labs', 'linux', 'sc', 'love', 'fax', 'php',
       'lp', 'tracking', 'thumbs', 'up', 'tw', 'campus', 'reg', 'digital', 'demo2', 'da', 'tr',
       'otrs', 'web6', 'ns02', 'mailgw', 'education', 'order', 'piwik', 'banners', 'rs', 'se',
       'venus', 'internal', 'webservices', 'cm', 'whois', 'sync', 'lb', 'is', 'code', 'click',
       'w2', 'bugzilla', 'virtual', 'origin-www', 'top', 'customer', 'pub', 'hotel', 'openx',
       'log', 'uat', 'cdn3', 'images0', 'cgi', 'posta', 'reseller', 'soft', 'movie', 'mba', 'n',
       'r', 'developer', 'nms', 'ns9', 'webcam', 'construtor', 'ebook', 'ftp3', 'join', 'dashboard',
       'bi', 'wpad', 'admin2', 'agent', 'wm', 'books', 'joomla', 'hotels', 'ezproxy', 'ds', 'sa',
       'sip1', 'consult', 'hrms', 'servicedesk', 'mail0', 'biz', 'images9', 'engage', 'tftp',
       'crm2', 'tollfree', 'system', 'fpt', 'legacy-www', 'discount', 'lab1', 'nag', 'pc', 'br',
       'robot', 'pop1', 'konfigurator', 'as', 'ns13', 'newsroom', 'address', 'read', 'bizmail',
       'tl', 'fed', 'owa2', 'nlb', 'media1', 'panel2', 'flash', 'sh', 'li', 'eps', 'quick',
       'ip1', 'people', 'ww1', 'tms', 'fw1', 'lock', 'ios', 'imagelib', 'relatorio', 'adserver2',
       'api2', 'domainname', 'maldives', 'aix', 'it2', 'adr', 'localhost2', 'stats2', 'suite',
       'engine', 'manage2', 'exchange2', 'records', 'find', 'll', 'mercury', 'central', 'varnish',
       'hd', 'myip', 'wss', 'unifi', 'banco', 'community2', 'secure2', 'intranet2', 'p2', 'www0',
       'career', 'tickets2', 'partners2', 'ntp2', 'e2', 'software2', 'sct', 'consultant', 'mail6',
       'ptz', 'ns15', 'dns6', 'admin1', 'websearch', 'svn2', 'support2', 'sys', 'estudante', 'voice',
       'bank', 'n1', 'analytics2', 'cpanel2', 'college', 'map2', 'dns5', 'mx4', 'mail7', 'proxy2',
       'cl', 'search2', 'staff2', 'backend', 'ip2', 'hospital', 'col', 'extranet2', 'domain2', 'vid',
       'health2', 'video2', 'info2', 'beta2', 'custom', 'med', 'images10', 'empresas', 'server3',
       'my2', 'galleries', 'registrar', 'data2', 'hotline', 'page', 'gps', 's5', 'blog2', 'img4',
       'money', 'www2cdn', 'community3', 'subdomain', 'imagem', 'dns7', 'central2', 'news2', 'cinema',
       'rep', 'web10', 'debug', 'treinamento', 'reporting', 'community4', 'public2', 'group', 'dev3',
       'cdn0', 'saas', 'media2', 'ag', 'cloud2', 'mobi', 'services2', 'film', '2', 'login2', 'g1',
       'parts', 'earth', 'cdn4', 'rc', 'devnet', 'it3', 'tour', 'healthcare', 'study', 'trade',
       'assets2', 'watch', 'demo1', 'feedback2', 'portal2', 'fr2', 'cloud3', 'connect2', 'file2',
       'c1', 'first', 'ai', 'dev4', 'pp', 'web20', 'message', 'sm', 'upload2', 'store2', 'web30',
       'intra2', 'internet', 'img0', 'globe', 'mobile2', 'ios2', 'queue', 'images11', 'news3', 'dr',
       'homepage', 'developer2', 'old2', 'host3', 'community5', 'lib2', 'policy', 'market2',
       'print', 'law', 'ipv6', 'dl2', 'mil', 'docs2', 'css2', 'ad2', 'test4', 'test5', 'net2',
       'mirror2', 'services3', 'my3', 'testserver', 'records2', 'cat', 'x', 'forum2', 'press2',
       'public3', 'media3', 'dynamic', 'testsite', 'bc', 'project2', 'free2', 'games2', 'assets3',
       'backend2', 'tv2', 'music2', 'tv3', 'site2', 'devsite', 'v3', 'register2', 'lab2', 'web7',
       'forums2', 'plugin', 'project3', 'test6', 'api3', 'search3', 'plus', 'p5', 'training2',
       'dns8', 'livestream', 'ipv4-1', 'extra', 'icon', 'web8', 'firewall2', 'news4', 'pc2',
       'policy2', 'pc3', 'plugin2', 'docs3', 'ibm', 'vol', 'web9', 'help2', 'ref', 'dns9', 'images12',
       'dns10', 'c4', 'profile', 'mars2', 'cloudflare', 'vid2', 'user2', 'search4', 'api4',
       'ftp4', 'mail8', 'support3', 'image2', 'cdn5', 'video3', 'system2', 'service2', 'web50',
       'dns11', 'www8', 'mail9', 'ecom', 'stage2', 'img5', 'map3', 'dns12', 'ad3', 'cdn6', 'img6',
       'dns13', 'api5', 'reg2', 'img7', 'file3', 'music3', 'public4', 'www9', 'r1', 'images13',
       'mailserver2', 'monitor2', 'secure3', 'cloud4', 'cdn7', 'market3', 'dns14', 'load', 'dns15',
       'health3', 'www10', 'video4', 'vpn3', 'content2', 'service3', 'help3', 'docs4', 'news5',
       'project4', 'service4', 'help4', 'ad4', 'img8', 'service5', 'img9', 'cdn8', 'files2',
       'img10', 'dns16', 'support4', 'video5', 'www11', 'secure4', 'api6', 'cdn9', 'e3', 'www12',
       'user3', 'images14', 'img11', 'help5', 'dns17', 'vpn4', 'www13', 'img12', 'video6', 'user4',
       'secure5', 'www14', 'www15', 'cdn10', 'img13', 'vpn5', 'secure6', 'help6', 'cloud5',
       'img14', 'vpn6', 'images15', 'files3', 'cdn11', 'files4', 'vpn7', 'video7', 'user5', 'cdn12',
       'files5', 'video8', 'www16', 'help7', 'images16', 'cdn13', 'video9', 'cdn14', 'www17',
       'files6', 'cdn15', 'www18', 'vpn8', 'www19', 'images17', 'files7', 'help8', 'cdn16',
       'files8', 'cdn17', 'www20', 'cdn18', 'files9', 'cdn19', 'files10', 'cdn20', 'www21', 'cdn21',
       'cdn22', 'files11', 'cdn23', 'files12', 'cdn24', 'www22', 'cdn25', 'cdn26', 'files13',
       'cdn27', 'files14', 'cdn28', 'cdn29', 'files15', 'cdn30', 'cdn31', 'cdn32', 'cdn33', 'cdn34',
       'cdn35', 'cdn36', 'cdn37', 'cdn38', 'cdn39', 'cdn40', 'cdn41', 'cdn42', 'cdn43', 'cdn44',
       'cdn45', 'cdn46', 'cdn47', 'cdn48', 'cdn49', 'cdn50'
    ]
 return subdomains

def subDomain_Scan(domain,subdomain_array):
 subdomain_store=[]
 count=0
 record_type=['A','AAAA','NS','CNAME','TXT','MX','PTR','SOA']
 resp = input("""\n  Enter the Scan option for the IP.
1. Simple DNS Name Scan
2. DNS-IP Scan
3. Comprehensive DNS Scan\n""")
 if resp=='1':
   for subdoms in subdomain_array:
    try :  
      sub_domain= resolver.resolve(f'{subdoms}.{domain}','A')
      if sub_domain:
          subdomain_store.append(f'{subdoms}.{domain}')
          if f"{subdoms}.{domain}" in subdomain_store:
            count=count+1
            print(f"{count}: {subdoms}.{domain}")
          else:
             pass  
    except resolver.NXDOMAIN:
       pass
    except resolver.NoAnswer:
       pass
    except KeyboardInterrupt:
       quit()
 elif resp=='2':
   for subdoms in subdomain_array: 
    try : 
      sub_domain= resolver.resolve(f'{subdoms}.{domain}','A')
      for server in sub_domain:
        if sub_domain:
          subdomain_store.append(f'{subdoms}.{domain}')
          if f"{subdoms}.{domain}" in subdomain_store:
            count=count+1
            print(f"{count}: {subdoms}.{domain} - {server} ")
          else:
             pass  
    except resolver.NXDOMAIN:
       pass
    except resolver.NoAnswer:
       pass
    except KeyboardInterrupt:
       quit()
 elif resp=='3':  
  for subdoms in subdomain_array:
    try : 
     for record in record_type: 
      sub_domain= resolver.resolve(f'{subdoms}.{domain}',record)
      print(f'{record} Records')
      print('-'*30)
      for server in sub_domain:
        if sub_domain:
          subdomain_store.append(f'{subdoms}.{domain}')
          if f"{subdoms}.{domain}" in subdomain_store:
            print(f"{subdoms}.{domain} - {server} ")
          else:
             pass  
    except resolver.NXDOMAIN:
       pass
    except resolver.NoAnswer:
       pass
    except KeyboardInterrupt:
       quit()
# Write to a text file

