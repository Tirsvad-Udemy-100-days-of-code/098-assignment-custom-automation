[English](Reflection) · [Dansk](Reflection-da) · **Bahasa Malaysia**

# Refleksi

## Bagaimana projek ini didekati

Kami merancang dahulu: kes perniagaan, analisis pihak berkepentingan, pelan projek dan lima pencapaian, masing-masing disemak sebelum kod ditulis. Kod kemudian dibina dalam lapisan kecil (domain, aplikasi, infrastruktur, baris arahan), setiap satu dengan ujian.

## Apa yang sukar

Menjadikan setiap langkah selamat. Pemindah fail boleh menghilangkan data, jadi pertembungan nama, fail yang dialihkan sebelum buat asal, dan muat turun yang belum siap masing-masing memerlukan peraturan dan ujian. Wiki dalam tiga bahasa juga memerlukan masa.

## Apa yang mudah

Pustaka standard melakukan hampir segalanya: `pathlib`, `shutil`, `json` dan `argparse`. Tiada pakej pihak ketiga diperlukan.

## Pembelajaran terbesar

Larian percubaan dan log buat asal menjadikan skrip yang berisiko sebagai alat yang boleh dipercayai. Automasi bukan sekadar menjimatkan masa, tetapi dapat melihat dan membatalkan apa yang dilakukan skrip.

## Apa yang akan dilakukan secara berbeza

Menambah lebih banyak peraturan, contohnya menyusun mengikut tarikh, dan fail tetapan untuk folder pengguna sendiri. Mengambil tangkapan skrin sejak awal semasa kod berkembang, bukan di hujung.
