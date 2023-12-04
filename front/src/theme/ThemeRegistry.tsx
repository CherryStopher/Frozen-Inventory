'use client'

import * as React from 'react'
import CssBaseline from '@mui/material/CssBaseline'
import { createTheme, ThemeProvider, type ThemeOptions } from '@mui/material/styles'
import { Roboto } from 'next/font/google'
import createCache from '@emotion/cache'
import { CacheProvider } from '@emotion/react'

const roboto = Roboto({
  weight: ['300', '400', '500', '700'],
  style: ['normal', 'italic'],
  subsets: ['latin']
})

const themeOptions: ThemeOptions = {
  typography: {
    fontSize: 12,
    fontFamily: roboto.style.fontFamily
  },
  palette: {
    background: {
      // pink
      default: '#E5E5E5'
    },
    primary: {
      main: '#1976d2'
    },
    text: {
      primary: '#300000'
    }
  },
  colors: {
    white: '#ffffff'
  }
}

export const theme = createTheme(themeOptions)
export const cache = createCache({ key: 'css' })

export default function ThemeRegistry ({
  children
}: {
  children: React.ReactNode
}): JSX.Element {
  return (
    <CacheProvider value={cache}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        {children}
      </ThemeProvider>
    </CacheProvider>
  )
}
