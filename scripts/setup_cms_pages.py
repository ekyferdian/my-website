import json
from pathlib import Path

root = Path('c:/Users/ACEH/Documents/web eky')
content_dir = root / 'content' / 'pages'
js_dir = root / 'js'
content_dir.mkdir(parents=True, exist_ok=True)
js_dir.mkdir(parents=True, exist_ok=True)

page_files = {
    'index': {
        'filename': 'index.html',
        'title': 'GameVerse ID - Portal Informasi Game Online & Casino',
        'description': 'Panduan, FAQ, dan artikel informatif untuk memahami berbagai game dengan lebih mudah.',
        'hero_title': 'Portal Informasi Game Online & Casino',
        'hero_text': 'Temukan panduan, FAQ, dan artikel informatif untuk memahami berbagai game dengan lebih mudah.',
        'hero_cta_text': 'Mulai Eksplorasi',
        'hero_cta_link': 'guide.html',
        'page_body': (
            '### Panduan Populer\n\n'
            '- **Panduan Pemula**: Pelajari dasar-dasar dan istilah penting.\n'
            '- **Strategi Dasar**: Memahami mekanik dan ritme permainan.\n'
            '- **FAQ Lengkap**: Jawaban dari pertanyaan paling umum.\n\n'
            '### Artikel Terbaru\n\n'
            '- **Memahami Dunia Game Modern**: Tips memahami perkembangan dan tren game.\n'
            '- **Istilah-Istilah Penting**: Pelajari terminologi yang sering digunakan.\n'
        ),
    },
    'article': {
        'filename': 'article.html',
        'title': 'Artikel Lengkap - GameVerse ID',
        'description': 'Artikel edukatif dan informasi terbaru seputar dunia game online.',
        'hero_title': 'Artikel',
        'hero_text': 'Informasi dan tips terbaru seputar dunia game.',
        'hero_cta_text': '',
        'hero_cta_link': '',
        'page_body': (
            '### Memahami Strategi Dasar dalam Game\n\n'
            'Banyak pemain langsung bermain tanpa memahami mekanik dasar permainan.\n\n'
            'Dengan memahami aturan, ritme permainan, serta pola strategi umum, pemain dapat lebih memahami pengalaman bermain.\n\n'
            '### Gunakan Konten Ini untuk Belajar\n\n'
            'Jelajahi panduan permainan, teknik taruhan, dan istilah penting untuk menjadi lebih percaya diri saat bermain.'
        ),
    },
    'guide': {
        'filename': 'guide.html',
        'title': 'Panduan - GameVerse ID',
        'description': 'Panduan permainan yang membantu kamu memahami setiap jenis game dan mekanik utama.',
        'hero_title': 'Panduan Permainan',
        'hero_text': 'Pelajari berbagai jenis permainan dan cara kerjanya.',
        'hero_cta_text': '',
        'hero_cta_link': '',
        'page_body': (
            '### Pilih Game yang Ingin Kamu Pelajari\n\n'
            '- [Blackjack](blackjack.html) – Permainan kartu mendekati angka 21.\n'
            '- [Baccarat](baccarat.html) – Bandingkan Player vs Banker.\n'
            '- [Roulette](roulette.html) – Prediksi angka pada roda.\n'
            '- [Poker](poker.html) – Kombinasi kartu terbaik untuk menang.\n'
            '- [Slots](slots.html) – Slot digital dengan simbol dan bonus.\n'
            '- [Togel](togel.html) – Permainan tebak angka.\n\n'
            'Setiap panduan menjelaskan aturan dasar, strategi penting, dan istilah yang sering muncul.'
        ),
    },
    'faq': {
        'filename': 'faq.html',
        'title': 'FAQ - GameVerse ID',
        'description': 'Pertanyaan umum mengenai website, permainan, dan cara menggunakan konten kami.',
        'hero_title': 'Pertanyaan Umum',
        'hero_text': 'Jawaban untuk pertanyaan yang sering diajukan.',
        'hero_cta_text': '',
        'hero_cta_link': '',
        'page_body': (
            '### Apa tujuan website ini?\n\n'
            'Memberikan informasi dan panduan game online.\n\n'
            '### Bagaimana memulai memahami game?\n\n'
            'Mulai dari aturan dasar, tips strategi, dan FAQ agar kamu lebih cepat paham.\n\n'
            '### Apakah ada update konten?\n\n'
            'Ya, artikel serta panduan akan diperbarui sesuai tren dan informasi terbaru.'
        ),
    },
    'tentang': {
        'filename': 'tentang.html',
        'title': 'Tentang Website - GameVerse ID',
        'description': 'Tentang GameVerse ID dan tujuan kami membantu pengguna memahami dunia game online.',
        'hero_title': 'Tentang Website',
        'hero_text': 'Mengenal lebih jauh tentang GameVerse ID.',
        'hero_cta_text': '',
        'hero_cta_link': '',
        'page_body': (
            '### Siapa Kami?\n\n'
            'Website ini dibuat untuk memberikan informasi, panduan, serta artikel edukatif seputar game online.\n\n'
            '### Misi Kami\n\n'
            'Membantu pemain baru dan berpengalaman memahami aturan, istilah, dan strategi dasar dalam berbagai permainan.'
        ),
    },
    'blackjack': {
        'filename': 'blackjack.html',
        'title': 'Blackjack - GameVerse ID',
        'description': 'Panduan Blackjack termasuk aturan dasar, strategi, dan nilai kartu.',
        'hero_title': 'Blackjack',
        'hero_text': 'Permainan kartu dengan target 21 yang menggabungkan strategi dan keberuntungan.',
        'hero_cta_text': 'Lihat Panduan',
        'hero_cta_link': 'guide.html',
        'page_body': (
            '### Pengenalan\n\n'
            'Blackjack adalah permainan kartu populer di kasino dan situs game. Tujuannya sederhana: mendapatkan nilai kartu sedekat mungkin dengan 21 tanpa melebihinya.\n\n'
            '### Aturan Dasar\n\n'
            '- Kartu angka (2–10) bernilai sesuai angka.\n'
            '- Kartu wajah (J, Q, K) bernilai 10.\n'
            '- As bisa bernilai 1 atau 11.\n'
            '- Pemain dan dealer masing-masing mendapat dua kartu di awal ronde.\n'
            '- Dealer biasanya harus Hit sampai minimal 17.\n\n'
            '### Tabel Nilai Kartu\n\n'
            '| Kartu | Nilai | Keterangan |\n'
            '| --- | --- | --- |\n'
            '| 2 - 10 | Angka kartu | Sesuai angka |\n'
            '| J, Q, K | 10 | Kartu wajah bernilai 10 |\n'
            '| As | 1 atau 11 | Sesuai kondisi terbaik |\n\n'
            '### Strategi Dasar\n\n'
            '- Hit ketika total kartu Anda 8–11.\n'
            '- Stand jika Anda mendapatkan 17 atau lebih.\n'
            '- Split ketika dua kartu awal bernilai sama.\n'
            '- Double Down saat total 9–11.\n'
            '- Kelola taruhan dengan bijak.\n'
        ),
    },
    'baccarat': {
        'filename': 'baccarat.html',
        'title': 'Baccarat - GameVerse ID',
        'description': 'Penjelasan Baccarat, aturan, dan cara menghitung nilai kartu.',
        'hero_title': 'Baccarat',
        'hero_text': 'Permainan cepat antara Player dan Banker dengan tujuan mendekati angka 9.',
        'hero_cta_text': 'Lihat Panduan',
        'hero_cta_link': 'guide.html',
        'page_body': (
            '### Pengenalan\n\n'
            'Baccarat adalah permainan kasino populer yang sederhana tetapi elegan. Pemain bisa memasang taruhan pada Player, Banker, atau Tie.\n\n'
            '### Aturan Dasar\n\n'
            '- Tujuannya mendapatkan nilai sedekat mungkin dengan 9.\n'
            '- Kartu 2–9 bernilai angka aslinya.\n'
            '- 10, J, Q, K bernilai 0.\n'
            '- As bernilai 1.\n'
            '- Jika total lebih dari 9, gunakan digit terakhir.\n\n'
            '### Tabel Nilai Kartu\n\n'
            '| Kartu | Nilai | Keterangan |\n'
            '| --- | --- | --- |\n'
            '| 2 - 9 | Angka aslinya | Contoh: 7 = 7 |\n'
            '| 10, J, Q, K | 0 | Tidak menambah total |\n'
            '| As | 1 | Nilai paling rendah |\n\n'
            '### Istilah Penting\n\n'
            '- **Player** – sisi pertama yang mendapatkan kartu.\n'
            '- **Banker** – sisi lawan dalam taruhan.\n'
            '- **Tie** – taruhan bahwa kedua sisi seri.\n'
            '- **Natural** – total awal 8 atau 9.\n'
        ),
    },
    'poker': {
        'filename': 'poker.html',
        'title': 'Poker - GameVerse ID',
        'description': 'Panduan Poker dengan kombinasi tangan, strategi, dan istilah penting.',
        'hero_title': 'Poker',
        'hero_text': 'Poker menguji strategi, membaca lawan, dan kombinasi tangan terbaik.',
        'hero_cta_text': 'Lihat Panduan',
        'hero_cta_link': 'guide.html',
        'page_body': (
            '### Pengenalan\n\n'
            'Poker adalah permainan kartu yang paling banyak dimainkan di dunia. Kemenangan ditentukan oleh kombinasi tangan paling kuat dan kemampuan membaca lawan.\n\n'
            '### Kombinasi Tangan\n\n'
            '| Tangan | Deskripsi |\n'
            '| --- | --- |\n'
            '| Royal Flush | 10-J-Q-K-As dalam satu warna |\n'
            '| Straight Flush | Lima kartu berurutan dalam satu warna |\n'
            '| Four of a Kind | Empat kartu bernilai sama |\n'
            '| Full House | Tiga kartu sama + pasangan |\n'
            '| Flush | Lima kartu satu warna |\n'
            '| Straight | Lima kartu berurutan |\n'
            '| Three of a Kind | Tiga kartu sama |\n'
            '| Two Pair | Dua pasangan |\n'
            '| Pair | Satu pasangan |\n'
            '| High Card | Kartu tertinggi |\n\n'
            '### Strategi Dasar\n\n'
            '- Perhatikan posisi dan peluang kartu.\n'
            '- Jangan terlalu sering bluff pada pemain ketat.\n'
            '- Naikkan taruhan saat tangan kuat.\n'
            '- Fold jika tangan lemah.\n'
        ),
    },
    'roulette': {
        'filename': 'roulette.html',
        'title': 'Roulette - GameVerse ID',
        'description': 'Panduan Roulette meliputi jenis taruhan, peluang, dan cara bermain.',
        'hero_title': 'Roulette',
        'hero_text': 'Permainan roda klasik dengan banyak pilihan taruhan sederhana dan kompleks.',
        'hero_cta_text': 'Lihat Panduan',
        'hero_cta_link': 'guide.html',
        'page_body': (
            '### Pengenalan\n\n'
            'Roulette adalah permainan kasino yang terkenal dengan roda berputar dan bola kecil. Pemain memasang taruhan pada angka, warna, atau kelompok angka.\n\n'
            '### Jenis Taruhan\n\n'
            '| Taruhan | Contoh | Peluang |\n'
            '| --- | --- | --- |\n'
            '| Merah / Hitam | Taruh warna | Hampir 50% |\n'
            '| Genap / Ganjil | Taruh angka genap atau ganjil | Hampir 50% |\n'
            '| Duzin | 12 angka berturut-turut | 1 banding 3 |\n'
            '| Kolom | Satu kolom angka | 1 banding 3 |\n'
            '| Angka Tunggal | Satu angka saja | 1 banding 37/38 |\n\n'
            '### Cara Bermain\n\n'
            '- Pilih taruhan sebelum roda diputar.\n'
            '- Tunggu bola berhenti pada angka.\n'
            '- Tentukan apakah ingin risiko rendah atau tinggi.\n'
            '- Perhatikan perbedaan antara roulette Eropa dan Amerika.\n'
        ),
    },
    'slots': {
        'filename': 'slots.html',
        'title': 'Slots - GameVerse ID',
        'description': 'Penjelasan Slots dengan simbol, fitur bonus, dan tips bermain.',
        'hero_title': 'Slots',
        'hero_text': 'Permainan gulungan digital dengan simbol, bonus, dan jackpot.',
        'hero_cta_text': 'Lihat Panduan',
        'hero_cta_link': 'guide.html',
        'page_body': (
            '### Pengenalan\n\n'
            'Slots adalah permainan kasino sederhana di mana Anda memutar gulungan untuk mencocokkan simbol. Slot modern memiliki fitur bonus, putaran gratis, dan banyak kombinasi kemenangan.\n\n'
            '### Fitur Utama\n\n'
            '- Wild: simbol pengganti untuk membuat kombinasi menang.\n'
            '- Scatter: bisa mengaktifkan putaran gratis atau bonus.\n'
            '- Bonus Game: mini game tambahan di dalam slot.\n'
            '- Jackpot Progresif: menang besar ketika jackpot tercapai.\n\n'
            '### Tabel Simbol\n\n'
            '| Simbol | Fungsi | Contoh |\n'
            '| --- | --- | --- |\n'
            '| Wild | Pengganti simbol lain | Mempermudah menang |\n'
            '| Scatter | Aktifkan putaran gratis | Biasanya 3+ scatter |\n'
            '| Bonus | Membuka mini game | Fitur ekstra |\n\n'
            '### Tips Bermain\n\n'
            '- Pelajari paytable sebelum memasang taruhan.\n'
            '- Atur batas taruhan supaya permainan tetap nyaman.\n'
            '- Manfaatkan putaran gratis bila tersedia.\n'
            '- Pilih slot dengan volatilitas yang sesuai gaya bermain Anda.\n'
        ),
    },
    'togel': {
        'filename': 'togel.html',
        'title': 'Togel - GameVerse ID',
        'description': 'Panduan Togel dengan jenis taruhan, pasaran, dan istilah penting.',
        'hero_title': 'Togel',
        'hero_text': 'Permainan tebakan angka populer dengan banyak pasaran dan variasi taruhan.',
        'hero_cta_text': 'Lihat Panduan',
        'hero_cta_link': 'guide.html',
        'page_body': (
            '### Format\n\n'
            '2D, 3D, dan 4D adalah jenis taruhan paling umum.\n\n'
            '### Pasaran\n\n'
            'Setiap pasaran memiliki jadwal undian dan pembayaran berbeda.\n\n'
            '### Cara Bermain\n\n'
            '- Pilih pasaran dan jenis taruhan.\n'
            '- Masukkan angka pilihan Anda dan tentukan nominal taruhan.\n'
            '- Konfirmasi taruhan dan tunggu hasil undian.\n'
            '- Jika angka cocok, klaim hadiah sesuai tabel pembayaran pasaran.\n\n'
            '### Istilah Penting\n\n'
            '- **Pasaran** – tempat atau jadwal undian.\n'
            '- **2D** – taruhan dua angka terakhir.\n'
            '- **3D** – taruhan tiga angka.\n'
            '- **4D** – taruhan empat angka.\n'
            '- **Hadiah** – pembayaran berdasarkan jenis taruhan.\n'
        ),
    },
}

html_template = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="navbar">
    <div class="container nav-wrap">
      <input type="checkbox" id="nav-toggle" class="nav-toggle" hidden />
      <label for="nav-toggle" class="burger" aria-label="Toggle menu">
        <span></span>
      </label>
      <div class="logo"><img src="GVID.png" alt="GVID logo"></div>
      <nav>
        <a href="index.html">Beranda</a>
        <a href="guide.html">Panduan</a>
        <a href="article.html">Artikel</a>
        <a href="faq.html">FAQ</a>
        <a href="tentang.html">Tentang</a>
      </nav>
    </div>
  </header>

  <section class="hero hero-small">
    <div class="container">
      <h1 id="hero-title">{hero_title}</h1>
      <p id="hero-text">{hero_text}</p>
      <a id="hero-cta" class="btn-primary" href="{hero_cta_link}" style="display: {cta_display};">{hero_cta_text}</a>
    </div>
  </section>

  <section class="section">
    <div class="container" id="page-body">
      <!-- Konten akan dimuat dari CMS -->
    </div>
  </section>

  <footer>
    <p>© 2026 Portal Informasi Game</p>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="js/page-content.js"></script>
</body>
</html>
'''

for slug, data in page_files.items():
    html_file = root / data['filename']
    cta_display = 'inline-block' if data['hero_cta_text'] else 'none'
    html_content = html_template.format(
        title=data['title'],
        description=data['description'],
        hero_title=data['hero_title'],
        hero_text=data['hero_text'],
        hero_cta_text=data['hero_cta_text'],
        hero_cta_link=data['hero_cta_link'] or '#',
        cta_display=cta_display,
    )
    html_file.write_text(html_content, encoding='utf-8')
    json_file = content_dir / f'{slug}.json'
    json_file.write_text(json.dumps({
        'title': data['title'],
        'description': data['description'],
        'hero_title': data['hero_title'],
        'hero_text': data['hero_text'],
        'hero_cta_text': data['hero_cta_text'],
        'hero_cta_link': data['hero_cta_link'],
        'page_body': data['page_body'],
    }, indent=2, ensure_ascii=False), encoding='utf-8')

page_content_js = '''const path = window.location.pathname;
const page = path.endsWith('/') || path === '/' ? 'index' : path.split('/').pop().replace('.html','');
const dataUrl = `content/pages/${page}.json`;

async function loadPageContent() {
  try {
    const response = await fetch(dataUrl);
    if (!response.ok) {
      console.warn(`Tidak dapat memuat konten halaman dari ${dataUrl}`);
      return;
    }
    const data = await response.json();
    if (data.title) document.title = data.title;
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc && data.description) metaDesc.content = data.description;
    const setText = (id, value) => {
      const el = document.getElementById(id);
      if (el && value) el.textContent = value;
    };
    setText('hero-title', data.hero_title);
    setText('hero-text', data.hero_text);
    const cta = document.getElementById('hero-cta');
    if (cta) {
      if (data.hero_cta_text) {
        cta.textContent = data.hero_cta_text;
        cta.href = data.hero_cta_link || '#';
        cta.style.display = 'inline-block';
      } else {
        cta.style.display = 'none';
      }
    }
    const pageBody = document.getElementById('page-body');
    if (pageBody) {
      pageBody.innerHTML = data.page_body ? marked.parse(data.page_body) : '';
    }
  } catch (error) {
    console.error('Gagal memuat konten halaman', error);
  }
}

loadPageContent();
'''

(js_dir / 'page-content.js').write_text(page_content_js, encoding='utf-8')

config_file = root / 'admin' / 'config.yml'
config_text = config_file.read_text(encoding='utf-8')
if 'name: "pages"' not in config_text and 'name: "pages"' not in config_text:
    pages_config = '''  - name: "pages"
    label: "Halaman"
    label_singular: "Halaman"
    files:
      - label: "Beranda"
        name: "home"
        file: "content/pages/index.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Teks Tombol CTA", name: "hero_cta_text", widget: "string", required: false}
          - {label: "Link Tombol CTA", name: "hero_cta_link", widget: "string", required: false}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Artikel"
        name: "article"
        file: "content/pages/article.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Panduan"
        name: "guide"
        file: "content/pages/guide.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "FAQ"
        name: "faq"
        file: "content/pages/faq.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Tentang"
        name: "tentang"
        file: "content/pages/tentang.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Blackjack"
        name: "blackjack"
        file: "content/pages/blackjack.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Teks Tombol CTA", name: "hero_cta_text", widget: "string", required: false}
          - {label: "Link Tombol CTA", name: "hero_cta_link", widget: "string", required: false}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Baccarat"
        name: "baccarat"
        file: "content/pages/baccarat.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Teks Tombol CTA", name: "hero_cta_text", widget: "string", required: false}
          - {label: "Link Tombol CTA", name: "hero_cta_link", widget: "string", required: false}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Poker"
        name: "poker"
        file: "content/pages/poker.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Teks Tombol CTA", name: "hero_cta_text", widget: "string", required: false}
          - {label: "Link Tombol CTA", name: "hero_cta_link", widget: "string", required: false}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Roulette"
        name: "roulette"
        file: "content/pages/roulette.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Teks Tombol CTA", name: "hero_cta_text", widget: "string", required: false}
          - {label: "Link Tombol CTA", name: "hero_cta_link", widget: "string", required: false}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Slots"
        name: "slots"
        file: "content/pages/slots.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Teks Tombol CTA", name: "hero_cta_text", widget: "string", required: false}
          - {label: "Link Tombol CTA", name: "hero_cta_link", widget: "string", required: false}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
      - label: "Togel"
        name: "togel"
        file: "content/pages/togel.json"
        fields:
          - {label: "Judul Halaman", name: "title", widget: "string"}
          - {label: "Deskripsi SEO", name: "description", widget: "text"}
          - {label: "Judul Hero", name: "hero_title", widget: "string"}
          - {label: "Deskripsi Hero", name: "hero_text", widget: "text"}
          - {label: "Teks Tombol CTA", name: "hero_cta_text", widget: "string", required: false}
          - {label: "Link Tombol CTA", name: "hero_cta_link", widget: "string", required: false}
          - {label: "Isi Halaman", name: "page_body", widget: "markdown"}
'''
    if config_text.strip().endswith(''):
        config_file.write_text(config_text + '\n' + pages_config, encoding='utf-8')
    else:
        config_file.write_text(config_text + '\n' + pages_config, encoding='utf-8')
else:
    print('Pages collection already exists in config.yml')
