import MarkdownIt from 'markdown-it';

export function createMarkdownParser() {
  const md = new MarkdownIt({
    html: false,
    linkify: true,
    typographer: true,
  });

  function addLineWordIds(md) {
    let line = 0;
    let word = 0;

    function addLineId(tokens, idx) {
      line += 1;
      tokens[idx].attrSet('data-line-id', `line-${line}`);
    }

    const blockTokens = [
      'paragraph_open',
      'heading_open',
      'blockquote_open',
      'list_item_open',
    ];

    blockTokens.forEach((type) => {
      const original =
        md.renderer.rules[type] ||
        function (tokens, idx, options, env, self) {
          return self.renderToken(tokens, idx, options);
        };
      md.renderer.rules[type] = function (tokens, idx, options, env, self) {
        addLineId(tokens, idx);
        return original(tokens, idx, options, env, self);
      };
    });

    const defaultText =
      md.renderer.rules.text ||
      function (tokens, idx, options, env, self) {
        return self.renderToken(tokens, idx, options);
      };
    md.renderer.rules.text = function (tokens, idx) {
      const content = tokens[idx].content;
      return content
        .split(/(\s+)/)
        .map((token) => {
          if (/\s+/.test(token)) return token;
          word += 1;
          return `<span data-word-id="word-${word}">${md.utils.escapeHtml(token)}</span>`;
        })
        .join('');
    };
  }

  md.use(addLineWordIds);
  return md;
}
