import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import path from "path"

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@/components/ui/marginalia-portfolio-template": path.resolve(
        __dirname,
        "./components/marginalia-portfolio-template/marginalia-portfolio-template.tsx"
      ),
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    port: 3000,
    open: true,
  },
})
