import { Card, CardContent, Typography } from '@mui/material'
import styles from './TransactionCard.module.css'

interface TransactionCardProps {
  title: string
  details: string[]
  value: number
}

export const TransactionCard: React.FC<TransactionCardProps> = ({
  title,
  details,
  value
}: TransactionCardProps) => {
  return (
    <Card className={styles.bigCardsContainer}variant="outlined">
      <CardContent>
        <Typography variant="subtitle1" component="div">
          {title}
        </Typography>
        <Typography variant="subtitle2">
          {details.map((detail) => (
            <div key={
              detail // TODO: fix this
            }>{detail}</div>
          ))}
          <br />
          <Typography variant="body1">{value}</Typography>
        </Typography>
      </CardContent>
    </Card>
  )
}
