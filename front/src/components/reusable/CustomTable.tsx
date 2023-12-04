'use client'
import {
  Table,
  TableContainer,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  TableSortLabel,
  TablePagination,
  Paper
} from '@mui/material'
import { useState } from 'react'
import { orderBy } from 'lodash'
import { useTheme } from '@mui/material/styles'

export interface CustomTableColumn {
  title: string
  attr: string
  width?: string | number
  minWidth?: string | number
  align?: TextAlign
}
export enum CustomTableRowDataType {
  TEXT = 'TEXT',
}
type CustomTableRowData = TextRowData

type TextAlign = 'left' | 'center' | 'right'

interface TextRowData {
  type: CustomTableRowDataType.TEXT
  sortValue?: any
  text: string
  align?: TextAlign
}

export interface CustomTableRow {
  data: Record<string, CustomTableRowData>
  onClick?: () => void
}

interface SortData {
  column: string
  order: 'desc' | 'asc'
}

export interface Sortable {
  excludeColumns?: string[]
  defaultValue?: SortData
}

export interface CustomTableProps {
  columns: CustomTableColumn[]
  data: CustomTableRow[]
  rowsPerPage?: number
  sortable?: Sortable
  maxHeight?: string
}

export const CustomTable: React.FC<CustomTableProps> = ({
  columns,
  data,
  sortable,
  maxHeight
}: CustomTableProps) => {
  const theme = useTheme()
  const [currentPage, setCurrentPage] = useState(0)
  const [rowsPerPage, setRowsPerPage] = useState(5)
  const [selectedSort, setSelectedSort] = useState<SortData | null>(
    () => sortable?.defaultValue ?? null
  )
  const havePagination = Boolean(rowsPerPage)
  const handleChangeRowsPerPage = (
    event: React.ChangeEvent<HTMLInputElement>
  ): void => {
    setRowsPerPage(parseInt(event.target.value, 10))
    setCurrentPage(0)
  }
  return (
    <>
      <TableContainer component={Paper} style={{
        maxHeight: maxHeight ?? undefined
      }}>
        <Table stickyHeader={!(maxHeight == null)}>
          <TableHead>
            <TableRow>
              {columns.map((col) => (
                <TableCell key={col.attr}>
                  {(sortable != null) &&
                  !(sortable.excludeColumns ?? []).includes(col.attr)
                    ? (
                    <TableSortLabel
                      active={selectedSort?.column === col.attr}
                      direction={selectedSort?.order}
                      onClick={() => {
                        setSelectedSort((prev) => {
                          if (prev == null || prev.column !== col.attr) {
                            return {
                              column: col.attr,
                              order: 'asc'
                            }
                          }
                          return {
                            column: col.attr,
                            order: prev.order === 'asc' ? 'desc' : 'asc'
                          }
                        })
                      }
                      }
                    >
                      {col.title}
                    </TableSortLabel>
                      )
                    : (
                        col.title
                      )}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {((selectedSort != null)
              ? orderBy(
                data,
                (item) => {
                  return item.data[selectedSort.column].type ===
                      CustomTableRowDataType.TEXT
                    ? (item.data[selectedSort.column])
                        .sortValue ?? null
                    : null
                },
                [selectedSort.order]
              )
              : data
            )
              .slice(
                havePagination ? currentPage * rowsPerPage : 0,
                havePagination
                  ? currentPage * rowsPerPage + rowsPerPage
                  : data.length
              )
              .map((d, idx) => (
                <TableRow key={idx} onClick={d.onClick}
                sx={{
                  '&:nth-of-type(odd)': {
                    backgroundColor: theme.colors.white
                  },
                  '&:nth-of-type(even)': {
                    backgroundColor: theme.palette.grey['100']
                  },
                  '& p': {
                    width: '100%',
                    whiteSpace: 'pre-line',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    display: '-webkit-box',
                    'WebkitLineClamp': 1,
                    'WebkitBoxOrient': 'vertical',
                    margin: 0,
                    padding: 0
                  }
                }}>
                  {columns.map((col) => (
                    <TableCell key={`${idx}-${col.attr}`}>
                      {d.data[col.attr].type ===
                        CustomTableRowDataType.TEXT && (
                        <TextComponent
                          col={col}
                          data={d.data[col.attr] }
                        />
                      )}
                    </TableCell>
                  ))}
                </TableRow>
              ))}
          </TableBody>
        </Table>
      </TableContainer>
      {havePagination && (
        <TablePagination
          component="div"
          count={data.length}
          rowsPerPage={rowsPerPage}
          page={currentPage}
          onPageChange={(_, newPage) => { setCurrentPage(newPage) }}
          labelDisplayedRows={({ from, to, count }) =>
            `${from}-${to} de ${count}`
          }
          rowsPerPageOptions={[5, 10]}
          onRowsPerPageChange={handleChangeRowsPerPage}
          labelRowsPerPage={'Filas por página'}
        />
      )}
    </>
  )
}

interface TableRowComponent<T> {
  col: CustomTableColumn
  data: T
}

const TextComponent: React.FC<TableRowComponent<TextRowData>> = ({
  col: { align: colAlign },
  data: { text, align }
}: TableRowComponent<TextRowData>) => {
  return <p style={{ textAlign: align ?? colAlign }}>{text}</p>
}

// interface TableStyleProps {
//   maxHeight: string | undefined
// }
