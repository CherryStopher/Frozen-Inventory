import { IconButton, type OutlinedInputProps, TextField } from '@mui/material'
import { Search, Clear } from '@mui/icons-material'
import { preventSubmit } from '@utils/index'
import styles from './TableSearcher.module.css'

interface TableSearcherProps {
  searchText: string
  changeSearchText: (text: string) => void
  placeholder: string
}

export const TableSearcher: React.FC<TableSearcherProps> = ({
  searchText,
  changeSearchText,
  placeholder
}: TableSearcherProps) => {
  return (
    <form noValidate autoComplete="off" onSubmit={preventSubmit}>
      <TextField
        className={styles.root}
        InputProps={
          {
            value: searchText,
            className: styles.input,
            placeholder,
            endAdornment:
              searchText === ''
                ? (
                <Search />
                  )
                : (
                <IconButton
                  size="small"
                  onClick={() => {
                    changeSearchText('')
                  }}
                >
                  <Clear />
                </IconButton>
                  )
          } satisfies Partial<OutlinedInputProps>
        }
        variant="outlined"
        onChange={(event) => {
          changeSearchText(event.target.value)
        }}
      />
    </form>
  )
}
