'use client'
import { Box, Divider, Typography } from '@mui/material'
import { TransactionCard } from '@components/reusable'
import { useTheme } from '@mui/material/styles'
import styles from './page.module.css'

const DailySalesPage = (): JSX.Element => {
  const theme = useTheme()
  return (
    <>
      <Box className={styles.root}
      style={{
        backgroundColor: theme.palette.background.default
      }}>
        <Typography variant="subtitle1" component="div">
          {'12 Enero, 2023'}
        </Typography>
        <Divider />
        <Box className={styles.bigCardsContainer}>
          <TransactionCard
            title={'Minuto Verde'}
            details={['Rancagua', '35 productos']}
            value={210000}
          />
          <TransactionCard
            title={'Master Fresh'}
            details={['Rancagua', '40 productos']}
            value={350000}
          />
          <TransactionCard
            title={'Supermercado Lider'}
            details={['Rancagua', '30 productos']}
            value={150000}
          />
        </Box>
        <Typography variant="h6" align="right" component="div">
          {'Total ventas: 542000'}
        </Typography>

        <Typography variant="subtitle1" component="div">
          {'11 Enero, 2023'}
        </Typography>
        <Divider />
        <Box className={styles.bigCardsContainer}>
          <TransactionCard
            title={'Minuto Rojo'}
            details={['Rancagua', '25 productos']}
            value={130000}
          />
          <TransactionCard
            title={'Miss Fresh'}
            details={['Rancagua', '30 productos']}
            value={250000}
          />
          <TransactionCard
            title={'Supermercado Jumbo'}
            details={['Rancagua', '10 productos']}
            value={450000}
          />
          <TransactionCard
            title={'Fruna'}
            details={['Santiago', '40 productos']}
            value={721000}
          />
        </Box>
        <Typography variant="h6" align="right" component="div">
          {'Total ventas: 1510000'}
        </Typography>
      </Box>
    </>
  )
}

export default DailySalesPage
