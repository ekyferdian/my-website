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
    function parseMarkdown(md) {
      if (typeof marked !== 'undefined') {
        return typeof marked.parse === 'function' ? marked.parse(md) : marked(md);
      }
      if (typeof window !== 'undefined' && window.marked) {
        return typeof window.marked.parse === 'function' ? window.marked.parse(md) : window.marked(md);
      }
      return md;
    }
    if (pageBody) {
      if (page === 'guide') {
        pageBody.innerHTML = '';

        const createPremiumCard = () => {
          const card = document.createElement('div');
          card.className = 'card premium-card';
          return card;
        };

        if (data.page_body) {
          const introCard = createPremiumCard();
          introCard.innerHTML = parseMarkdown(data.page_body);
          pageBody.appendChild(introCard);
        }

        const guideItems = await loadGuideList();
        if (guideItems.length > 0) {
          const grid = document.createElement('div');
          grid.className = 'card-grid';

          guideItems.forEach(item => {
            const card = createPremiumCard();
            const h3 = document.createElement('h3');
            h3.textContent = item.title || 'Panduan';
            card.appendChild(h3);
            if (item.summary) {
              const p = document.createElement('p');
              p.textContent = item.summary;
              card.appendChild(p);
            }
            if (item.url) {
              const btn = document.createElement('a');
              btn.className = 'btn-primary';
              btn.href = item.url;
              btn.textContent = 'Pelajari';
              card.appendChild(btn);
            }
            grid.appendChild(card);
          });

          pageBody.appendChild(grid);
        } else {
          const emptyCard = createPremiumCard();
          const p = document.createElement('p');
          p.textContent = 'Belum ada panduan permainan. Tambahkan item panduan baru melalui CMS.';
          emptyCard.appendChild(p);
          pageBody.appendChild(emptyCard);
        }
      } else {
        pageBody.innerHTML = data.page_body ? parseMarkdown(data.page_body) : '';

        // Group content into cards by heading (H2/H3). Each heading starts a new card.
        const nodes = Array.from(pageBody.childNodes);
        const frag = document.createDocumentFragment();
        let currentCard = null;

        function createPremiumCard() {
          const card = document.createElement('div');
          card.className = 'card premium-card';
          return card;
        }

        function startNewCard() {
          currentCard = createPremiumCard();
          frag.appendChild(currentCard);
        }

        nodes.forEach(n => {
          if (n.nodeType === Node.ELEMENT_NODE) {
            const el = /** @type {HTMLElement} */ (n);
            const tag = el.tagName.toUpperCase();
            if (tag === 'H2' || tag === 'H3') {
              // start a new card containing this heading
              startNewCard();
              currentCard.appendChild(el);
              return;
            }
          }

          // For text nodes or other elements, append to current card; if none, create one
          if (!currentCard) startNewCard();
          currentCard.appendChild(n);
        });

        // Replace contents with grouped cards
        pageBody.innerHTML = '';
        pageBody.appendChild(frag);
      }
    }
    if (page === 'article') {
      await loadArticleList();
    }
  } catch (error) {
    console.error('Gagal memuat konten halaman', error);
  }
}

async function loadGuideList() {
  try {
    const response = await fetch('content/pages/guides.json');
    if (!response.ok) {
      return [];
    }
    const data = await response.json();
    return Array.isArray(data.guides) ? data.guides : [];
  } catch (error) {
    console.error('Gagal memuat daftar panduan', error);
    return [];
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
    // Build a card that contains the article list and a grid of article cards (with buttons)
    const listCard = document.createElement('div');
    listCard.className = 'card premium-card';
    const heading = document.createElement('h2');
    heading.textContent = 'Daftar Artikel';
    listCard.appendChild(heading);

    if (articles.length === 0) {
      const p = document.createElement('p');
      p.textContent = 'Belum ada artikel. Tambahkan artikel melalui CMS di bagian Daftar Artikel.';
      listCard.appendChild(p);
    } else {
      const grid = document.createElement('div');
      grid.className = 'card-grid';
      articles.forEach(article => {
        const url = article.url || '#';
        const card = document.createElement('div');
        card.className = 'card premium-card';
        const h3 = document.createElement('h3');
        h3.textContent = article.title || 'Tanpa Judul';
        const p = document.createElement('p');
        p.textContent = article.summary || 'Ringkasan belum diisi.';
        const btn = document.createElement('a');
        btn.className = 'btn-primary';
        btn.href = url;
        btn.textContent = 'Baca';
        card.appendChild(h3);
        card.appendChild(p);
        card.appendChild(btn);
        grid.appendChild(card);
      });
      listCard.appendChild(grid);
    }

    pageBody.appendChild(listCard);
  } catch (error) {
    console.error('Gagal memuat daftar artikel', error);
  }
}

loadPageContent();

