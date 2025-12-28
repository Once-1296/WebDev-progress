import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  root: ".", // ensures vite looks for index.html here
  build: {
    outDir: "dist",
  },
  server: {
    port: 5173,
    open: true, // auto-open browser
  },
})
