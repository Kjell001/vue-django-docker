import js from "@eslint/js"
import pluginVue from "eslint-plugin-vue"
import eslintConfigPrettier from "eslint-config-prettier"

export default [
  js.configs.recommended,
  ...pluginVue.configs["flat/recommended"],
  eslintConfigPrettier,
  {
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
  }
]