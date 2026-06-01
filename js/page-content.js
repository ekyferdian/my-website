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
  } catch (error) {
    console.error('Gagal memuat konten halaman', error);
  }
}

loadPageContent();
