import { defineConfig } from "eslint/config"
import globals from "globals"
import js from "@eslint/js"
import pluginVue from "eslint-plugin-vue"
import eslintConfigPrettier from "eslint-config-prettier"

export default defineConfig([
  js.configs.recommended,
  ...pluginVue.configs["flat/recommended"],
  eslintConfigPrettier,
  {
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
      },
    },
    rules: {
      "no-unused-vars": [
        "error",
        {
          argsIgnorePattern: "^_",
          varsIgnorePattern: "^_",
        },
      ],
      "vue/block-order": [
        "error",
        {
          order: [
            "template",
            "script:not([setup])",
            "script[setup]",
            "style:not([scoped])",
            "style[scoped]",
          ],
        },
      ],
      "vue/component-api-style": ["error", ["script-setup"]],
    },
  },
])
