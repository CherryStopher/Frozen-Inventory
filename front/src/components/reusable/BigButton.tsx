import React from 'react'
import { Button } from '@mui/material'
import styles from './BigButton.module.css'
import { useTheme } from '@mui/material/styles'

export interface BigButtonProps {
  onClick: () => void
  children: string
}

export const BigButton: React.FC<BigButtonProps> = ({ onClick, children }) => {
  const theme = useTheme()
  return (
    <Button onClick={onClick} className={styles.bigButton} style={{
      backgroundColor: theme.palette.primary.main,
      color: theme.colors.white
    }}>
      {children}
    </Button>
  )
}
