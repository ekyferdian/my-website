const path = window.location.pathname;
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
    if (page === 'article') {
      await loadArticleList();
    }
  } catch (error) {
    console.error('Gagal memuat konten halaman', error);
  }
}

async function loadArticleList() {
  try {
    const response = await fetch('content/articles/index.json');
    if (!response.ok) {
      return;
    }
    const data = await response.json();
    const pageBody = document.getElementById('page-body');
    if (!pageBody) return;

    const articles = Array.isArray(data.articles) ? data.articles : [];
    const listSection = document.createElement('div');
    listSection.className = 'article-list';

    if (articles.length === 0) {
      listSection.innerHTML = '<p>Belum ada artikel. Tambahkan artikel melalui CMS di bagian Daftar Artikel.</p>';
    } else {
      const items = articles.map(article => {
        const url = article.url || '#';
        return `
          <a class="card article-card" href="${url}">
            <h3>${article.title || 'Tanpa Judul'}</h3>
            <p>${article.summary || 'Ringkasan belum diisi.'}</p>
          </a>
        `;
      }).join('');

      listSection.innerHTML = `
        <h2>Daftar Artikel</h2>
        <div class="card-grid">${items}</div>
      `;
    }

    pageBody.appendChild(listSection);
  } catch (error) {
    console.error('Gagal memuat daftar artikel', error);
  }
}

loadPageContent();
