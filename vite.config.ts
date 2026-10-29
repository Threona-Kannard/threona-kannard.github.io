import { sveltekit } from "@sveltejs/kit/vite";
import { enhancedImages } from "@sveltejs/enhanced-img";
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
import { viteStaticCopy } from "vite-plugin-static-copy";

export default defineConfig({
    plugins: [enhancedImages(), tailwindcss(), sveltekit(),
    viteStaticCopy({
        targets: [
            {
                src: "src/lib/assets",
                dest: "src/lib/assets",
            },
        ],
    })],
});
