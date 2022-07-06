pip3 install tldextract
wget https://www.usom.gov.tr/url-list.txt
wget https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/ALL-phishing-domains.tar.gz
tar xzvf ALL-phishing-links.tar.gz
mv url-list.txt domain
mv ALL-phishing-links.txt domain2 
perl -pi -e 's/127.0.0.1//g' domain
perl -pi -e 's/0.0.0.0//g' domain
perl -pi -e 's/127.0.0.1//g' domain2
perl -pi -e 's/0.0.0.0//g' domain2
