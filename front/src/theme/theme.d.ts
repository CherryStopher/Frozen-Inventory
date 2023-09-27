import '@mui/material/styles'

declare module '@mui/material/styles' {
  interface Theme {
    colors: {
      white: string
    }
  }
  interface ThemeOptions {
    colors: {
      white: React.CSSProperties['color']
    }
  }
  // To add colors in palette when using createTheme
  interface Palette {
    neutral: PaletteColor
  }
  interface PaletteOptions {
    neutral?: PaletteColorOptions
  }
  interface PaletteColor {
    darker?: string
  }
  interface SimplePaletteColorOptions {
    darker?: string
  }
}
