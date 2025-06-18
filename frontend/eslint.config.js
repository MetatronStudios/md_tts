import vue from 'eslint-plugin-vue';
import vueParser from 'vue-eslint-parser';

export default [
  {
    files: ['**/*.vue', '**/*.js'],
    ignores: ['node_modules'],
    languageOptions: {
      parser: vueParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
      },
    },
    plugins: {
      vue,
    },
    rules: {
      ...vue.configs['flat/essential'].rules,
    },
  },
];
