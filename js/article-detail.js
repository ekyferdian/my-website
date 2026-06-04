function parseFrontmatter(markdown) {
  const fmMatch = markdown.match(/^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/);
  if (!fmMatch) {
    return { metadata: {}, body: markdown };
  }
  const metadata = {};
  const [_, frontmatter, body] = fmMatch;
  frontmatter.split(/\r?\n/).forEach(line => {
    const [key, ...rest] = line.split(':');
    if (!key) return;
    metadata[key.trim()] = rest.join(':').trim();
  });
  return { metadata, body };
}

function getQueryParam(name) {
  return new URLSearchParams(window.location.search).get(name);
}

async function loadArticle() {
  const articleDetail = document.getElementById('article-detail');
  const heroTitle = document.getElementById('hero-title');
  const heroText = document.getElementById('hero-text');

  const file = getQueryParam('file');
  if (!file) {
    articleDetail.innerHTML = '<p>Artikel tidak ditemukan. Kembali ke <a href="article.html">daftar artikel</a>.</p>';
    return;
  }

  try {
    const response = await fetch(`content/articles/${encodeURIComponent(file)}`);
    if (!response.ok) {
      articleDetail.innerHTML = '<p>Gagal memuat artikel. Pastikan nama file benar.</p>';
      return;
    }

    const raw = await response.text();
    const { metadata, body } = parseFrontmatter(raw);
    const title = metadata.title || 'Artikel tanpa judul';
    const description = metadata.description || '';

    document.title = `${title} - GameVerse ID`;
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.content = description || 'Detail artikel GameVerse ID.';
    if (heroTitle) heroTitle.textContent = title;
    if (heroText) heroText.textContent = description || 'Baca ulasan lengkapnya di bawah ini.';

    articleDetail.innerHTML = `
      <article>
        <h2>${title}</h2>
        ${description ? `<p>${description}</p>` : ''}
        ${marked.parse(body)}
      </article>
    `;
  } catch (error) {
    articleDetail.innerHTML = '<p>Terjadi kesalahan saat memuat artikel.</p>';
    console.error(error);
  }
}

loadArticle();
