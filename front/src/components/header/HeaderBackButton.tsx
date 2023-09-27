import React from 'react'
import { IconButton } from '@mui/material'
import ArrowBackIcon from '@mui/icons-material/ArrowBack'
import styles from './HeaderBackButton.module.css'
import { useTheme } from '@mui/material/styles'

interface HeaderBackButtonProps {
  onClick: () => void
}

export const HeaderBackButton: React.FC<HeaderBackButtonProps> = ({
  onClick
}) => {
  const theme = useTheme()
  return (
    <IconButton onClick={onClick} className={styles.root}
    sx={{
      color: theme.colors.white,
      backgroundColor: theme.palette.primary.main
    }}>
      <ArrowBackIcon />
    </IconButton>
  )
}
