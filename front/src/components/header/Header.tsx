'use client'

import { AppBar, Box, Typography } from '@mui/material'
import { usePathname, useRouter } from 'next/navigation'
import { type AppRoute, AppRouteNames, routeTabs } from '@/interfaces/index'
import { NavigationTabs } from '@components/header/NavigationTabs'
import styles from './Header.module.css'
import { HeaderBackButton } from '@components/header/HeaderBackButton'

export const Header = (): JSX.Element => {
  const router = useRouter()
  const pathname: AppRoute = usePathname() as AppRoute
  const addGoBackButton = !routeTabs.includes(pathname)
  return (
    <AppBar position="static">
      <Box className={styles.headerContainer}>
        <Box className={styles.titleContainer}>
          {addGoBackButton && <HeaderBackButton onClick={() => { router.back() }} />}
          <Typography variant="h4" className={styles.pageName}>
            {AppRouteNames[pathname]}
          </Typography>
        </Box>
        <NavigationTabs currentPath={pathname}/>
      </Box>
    </AppBar>
  )
}
