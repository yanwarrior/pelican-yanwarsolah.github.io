Title: Namedtuple Python, Apa dan Bagaimana ?
Date: 2016-12-10 19:34
Category: Python 3
Tags: python, namedtuple, collections
Slug: namedtuple-python-apa-dan-bagaimana
Authors: Yanwar Solahudin

Dengan `namedtuple`, kita bisa mengelompokan field-field tertentu seperti halnya class. 
`namedtuple` bisa di import dari module `collections`. dengan `namedtuple` kita bisa
mengisi field-field yang dikelompokan tersebut dengan nilai apapun kedalamnya, asalkan
nama field tersebut sudah diregister saat membuat instance `namedtuple`.

Asumsikan di sini kita memiliki objek `Mahasiswa` dimana objek ini memiliki field 
`nim`, `nama` dan `email`. kita bisa mengelompokan field-field tersebut menjadi satu
kelompok, yaitu kelompok `Mahasiswa`:

```Python
from collections import namedtuple

Mahasiswa = namedtuple("Mahasiswa", ['nim', 'nama', 'email'])

# Buat instance Mahasiswa
mhs = Mahasiswa('1111503007', 'Yanwar Solahudin', 'yanwarsolah@gmail.com')

# Cetak mahasiswa
print(mhs.nim)
print(mhs.nama)
print(mhs.email)
```

Kode di atas menghasilkan:

```
1111503007
Yanwar Solahudin
yanwarsolah@gmail.com
```

## Method _make

adakalanya kita ingin mengeset nilai-nilai field secara langsung melalui list. 
kita bisa melakukannya dengan bantuan method `_make`:

```python
data_mahasiswa = ['1111245223', 'John Smith', 'johnsmith@example.com']
mhs = Mahasiswa._make(data_mahasiswa)

print(mhs)
```

Kode di atas menghasilkan:

```
Mahasiswa(nim='1111245223', nama='John Smith', email='johnsmith@example.com')
```

Lebih Lambat ?
--------------

Setelah pengujian dengan JIT Compiler (PyPy), Namedtuple masih dibilang lambat. 
di sini kita bisa mengujinya dengan pengujian sederhana yang menghasilkan waktu
eksekusi dari `namedtuple` dan `tuple`. mana yang lebih cepat dan mana yang lebih lambat:

```Python
from collections import namedtuple
import time

# Membuat instance namedtuple
MahasiswaNT = namedtuple('MahasiswaNT', ['nim', 'nama', 'email'])

# Set waktu mulai
waktu_mulai = time.time()

# Proses 10000000 kali iterasi untuk namedtuple
i = 0
while i < 10000000:
	a = MahasiswaNT('1111503007', 'Yanwar Solahudin', 'yanwarsolah@gmail.com')
	if a[0] != '1111503007':
		raise Exception()
	i += 1

# Cetak waktu selesai iterasi untuk namedtuple
print("namedtuple\t= {0:.2f}\tDetik".format(time.time() - waktu_mulai))

# Set waktu mulai kembali
waktu_mulai = time.time()

# Proses 10000000 kali iterasi untuk tuple
i = 0
while i < 10000000:
	a = ('1111503007', 'Yanwar Solahudin', 'yanwarsolah@gmail.com')
	if a[0] != '1111503007':
		raise Exception()
	i += 1

# Cetak waktu selesai iterasi untuk tuple
print("tuple\t\t= {0:.2f}\tDetik".format(time.time() - waktu_mulai))
```

Kode di atas menghasilkan:

```
namedtuple	= 20.93	Detik
tuple		= 5.23	Detik
```

Sekarang, kita sudah mendapatkan hasilnya dan bisa menilai sendiri 
dengan asumsi kita masing-masing. ini hanyalah pengujian sederhana
yang menunjukan bahwa `namedtuple` lebih lambat dari pada menggunakan
`tuple` (native) Python.