# Simple-Nmap
 Scan your own pc
--TR--
<h2>Python Port Tarayıcı</h2>

<p><em>Bu proje, Python ile yazılmış basit bir port tarayıcıdır. Yerel makinenizdeki açık portları tarar ve bunları hizmet adlarıyla birlikte gösterir.</em></p>

<h2>Gereksinimler</h2>

<p><em>Aşağıdaki Python paketlerinin yüklü olduğundan emin olun:</em></p>
<ul>
  <li><em>socket</em></li>
  <li><em>threading</em></li>
</ul>

<h2>Kurulum</h2>

<p><em>Depoyu klonlayın:</em></p>
<pre><code>git clone https://github.com/kullanıcıadınız/port-tarayici.git
cd port-tarayici</code></pre>

<h2>Kullanım</h2>

<p><em>Script'i çalıştırın:</em></p>
<pre><code>python port_tarayici.py</code></pre>

<h2>Çıktı</h2>

<p><em>Script, IP adresinizi gösterir ve açık portları taramaya başlar. Açık portlar ve ilgili hizmet adları listelenir:</em></p>
<pre><code>IP Adresiniz: 192.168.1.5
192.168.1.5 üzerindeki açık portlar taranıyor...
Açık portlar:
Port 22: ssh
Port 80: http
Port 443: https
...</code></pre>








--EN--
<h2>Python Port Scanner</h2>
<p><em>This project is a simple port scanner written in Python. It scans the open ports on your local machine and displays them along with their service names.</em></p>
<h2>Requirements</h2>

<p><em>Ensure you have the following Python packages installed:</em></p>
<ul>
  <li><em>socket</em></li>
  <li><em>threading</em></li>
</ul>

<h2>Installation</h2>

<p><em>Clone the repository:</em></p>
<pre><code>git clone https://github.com/yourusername/port-scanner.git
cd port-scanner</code></pre>

<h2>Usage</h2>

<p><em>Run the script:</em></p>
<pre><code>python port_scanner.py</code></pre>

<h2>Output</h2>

<p><em>The script will display your IP address and start scanning open ports. Open ports and their corresponding service names will be listed:</em></p>
<pre><code>Your IP Address is: 192.168.1.5
Scanning open ports on 192.168.1.5...
Open ports:
Port 22: ssh
Port 80: http
Port 443: https
...</code></pre>
