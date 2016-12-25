Title: Storage Pada Cordova (Part 1)
Date: 2016-12-25 11:59
Category: JavaScript
Tags: JavaScript, Cordova, Mobile, Development, Cordova
Slug: storage-pada-cordova-1
Authors: Yanwar Solahudin


Storage atau penyimpanan pada cordova tidak lepas dari API storage pada HTML 5. banyak yang menyebutnya sebagai `local storage`. dengan memanfaatkan API local storage ini, kita bisa menyimpan data secara lokal di dalam browser. 

Sebelumnya, banyak yang menyimpan data pada cookies. tentunya berbeda dengan storage milik HTML 5 karena local storage lebih aman dan data yang disimpan bisa dalam jumlah yang lebih besar dari pada data cookies tanpa mengganggu performa aplikasi. Bukan berarti local storage bisa menyimpan data yang sangat besar, namun local storage memiliki batas-batas memori yang jauh lebih besar dari cookies (setidaknya sekitar 5mb).

Data pada local storage tidak akan di transfer ke server. penyimpanan data pada local storage disimpan per domain atau per protokol. Jadi, semua halaman bisa menyimpan dan mengakses data yang sama.

Pada tutorial ini kita akan belajar bagaimana memanfaatkan `local storage` pada cordova untuk menyimpan, menampilkan dan menghapus data pada local storage.

## Persiapan

Buka command line, ketik perintah berikut untuk membuat project cordova:

```
cordova create latihStorageApp com.latihan.latihstorageapp LatihStorageApp
```

Selanjutnya masuk ke dalam direktori project `latihSorageApp`:

```
cd latihStorageApp
```

Untuk sekadar latihan, kita hanya perlu menjalankan aplikasi cordova kita di browser saja. ketik perintah berikut ini untuk menambahkan platform browser:

```
cordova platform add browser
```

## Membuat Form

Pada file `www/index.html`, pada bagian `body` ubah kodenya menjadi seperti ini:

```html
<body>
        <div class="app">
            <h1>Latihan Local Storage</h1>
            <div>
                <p><input type="text" name="nim" id="txt_nim"></p>
                <p><input type="text" name="nama" id="txt_nama"></p>
                <p>
                    <button id="btn_simpan">Simpan</button>
                    <button id="btn_tampil">Tampil</button>
                    <button id="btn_ubah">Ubah</button>
                </p>
            </div>
        </div>
        <script type="text/javascript" src="cordova.js"></script>
        <script type="text/javascript" src="js/index.js"></script>
</body>
```

### Menambahkan Event Untuk Menyimpan Data

Kita akan menambahkan event untuk menyimpan data dengan cara membuat event listener pada `button` dengan id `btn_simpan`. ketika kita menekan tombol `Simpan`, semua data yang kita input ke inputan `nim` dan `nama` akan disimpan ke dalam local storage. sekarang buka file `www/js/index.js` dan tambahkan kode berikut:

```javascript
var latihan = {
    __init__: function() {
        this.simpan;
    },

    simpan: document.getElementById('btn_simpan').addEventListener('click', function() {
        var nim = document.getElementById('txt_nim').value;
        var nama = document.getElementById('txt_nama').value; 

        localStorage.setItem("nim", nim);
        localStorage.setItem("nama", nama);
        
        document.getElementById('txt_nim').value = "";
        document.getElementById('txt_nama').value = ""; 
    }),

    
};

latihan.__init__();
```

Pada kode di atas, terdapat method `__init__`,  atribut `simpan`. dimana method `__init__` digunakan untuk inisialisasi sebelum terjadinya event. pada atribut `simpan` berisi event untuk menyimpan data.

Sekarang, ketik perintah berikut ini untuk menjalankan aplikasi kita di browser:

```
cordova run browser
```

Secara otomatis, browser akan terbuka dan menampilkan halaman `index.html` seperti berikut:

![Tampilan Awal]({filename}/images/cordova-save.jpg)

Isi text inputan dengan nim dan nama, misalnya nim `1111503007` dan nama `Yanwar Solahudin` setelah itu klik tombol `Simpan`. Untuk melihat local storage, buka mode Inspect dengan menekan key `Ctrl + Shift + i` untuk Chrome. pada bagian tab `Application` pilih `Storage` (sebelah kiri):

![Local Storage]({filename}/images/local-storage.jpg)

Hasilnya akan terlihat seperti ini:

![Simpan Data]({filename}/images/cordova-save-1.jpg)

Gimana ? Mudah kan ? nantikan tutorial berikutnya untuk mengedit dan menghapus data. terimakasih. 






