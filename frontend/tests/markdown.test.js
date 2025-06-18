import { describe, it, expect } from 'vitest';
import { createMarkdownParser } from '../src/utils/markdown';

describe('markdown parser', () => {
  it('adds line and word ids', () => {
    const md = createMarkdownParser();
    const html = md.render('# Title\n\nHello world');
    expect(html).toContain('data-line-id="line-1"');
    expect(html).toContain('data-line-id="line-2"');
    expect(html).toContain('data-word-id="word-1"');
    expect(html).toContain('data-word-id="word-2"');
  });
});
