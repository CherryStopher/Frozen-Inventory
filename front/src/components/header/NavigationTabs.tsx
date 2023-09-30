'use client'
import { Tabs, Tab } from '@mui/material'
import { useTheme } from '@mui/material/styles'

import {
  type AppRoute,
  AppRouteNames,
  routeTabs,
  groupedAppRouteTabs
} from '@interfaces/routes'
import Link from 'next/link'

interface TabBarProps {
  currentPath: AppRoute
}

interface LinkTabProps {
  label?: string
  href?: string
  value?: string
}

function LinkTab (props: LinkTabProps): JSX.Element {
  return (
    <Tab
      LinkComponent={Link}
      {...props}
    />
  )
}

export const NavigationTabs = ({ currentPath }: TabBarProps): JSX.Element => {
  const theme = useTheme()
  return (
    <Tabs
    value={groupedAppRouteTabs[currentPath]}
    textColor='inherit'
    TabIndicatorProps={{
      style: { backgroundColor: theme.colors.white }
    }}
    >
      {routeTabs.map(
        (route: AppRoute) => (
          <LinkTab
            key={route}
            label={AppRouteNames[route]}
            value={route}
            href={route}/>
        ))}
    </Tabs>
  )
}
