'use client'
import { useState, useMemo } from 'react'
import { Box, Paper } from '@mui/material'
import {
  CustomTable,
  type CustomTableColumn,
  type CustomTableRow,
  CustomTableRowDataType,
  type Sortable,
  BigButton,
  TableSearcher
} from '@components/reusable'
import { AddSupplierModal } from '@components/suppliers'
import Fuse from 'fuse.js'
import { type Supplier } from '@interfaces/index'
import { useTheme } from '@mui/material/styles'
import styles from './page.module.css'

const tableSort: Sortable = {
  defaultValue: {
    column: 'name',
    order: 'desc'
  }
}

const inventoryCols: CustomTableColumn[] = [
  {
    title: 'Proveedor',
    attr: 'name'
  },
  {
    title: 'Nombre contacto',
    attr: 'contactName'
  },
  {
    title: 'Categoría',
    attr: 'category'
  },
  {
    title: 'Teléfono',
    attr: 'phone'
  },
  {
    title: 'Correo',
    attr: 'email'
  },
  {
    title: 'Dirección',
    attr: 'address'
  }
]

const suppliersData: Supplier[] = [
  {
    id: 1,
    name: 'Minuto Verde',
    contactName: 'Armando Esteban Quito',
    category: 'Congelados',
    phone: '+569 1234 5678',
    email: 'minutoverde@gmail.com',
    address: 'Av. Cachapoal #164',
    commune: 'Rancagua'
  }
]

const fuseOptions = {
  keys: ['name', 'category']
}

const SuppliersPage = (): JSX.Element => {
  const theme = useTheme()
  const [openModal, setOpenModal] = useState(false)

  const [searchText, setSearchText] = useState<string>('')
  const fuse = useMemo(
    () => new Fuse(suppliersData, fuseOptions),
    []
  )
  const filteredSuppliers: Supplier[] = useMemo(() => {
    if (searchText.length < 2) {
      return suppliersData
    }
    return fuse.search(searchText).map((el) => el.item)
  }, [searchText, fuse])
  const tableSuppliers: CustomTableRow[] = useMemo(() => {
    return filteredSuppliers.map((supplier) => ({
      data: {
        name: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.name
        },
        contactName: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.contactName
        },
        category: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.category
        },
        phone: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.phone
        },
        email: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.email
        },
        address: {
          type: CustomTableRowDataType.TEXT,
          text: `${supplier.address}, ${supplier.commune}`
        }
      }
    }))
  }, [filteredSuppliers])
  return (
    <>
      <Box
      className={styles.root}
      sx={{
        backgroundColor: theme.palette.background.default
      }}>
        <AddSupplierModal
          open={openModal}
          handleClose={() => { setOpenModal(false) }}
        />
        <Paper elevation={0} className={styles.tableContainer}>
          <TableSearcher
            searchText={searchText}
            changeSearchText={setSearchText}
            placeholder={'Buscar por proveedor o categoría'}
          />
          <CustomTable
            columns={inventoryCols}
            data={tableSuppliers}
            sortable={tableSort}
          />
        </Paper>
        <Box className={styles.bigButtonsContainer}>
          <BigButton onClick={() => { setOpenModal(true) }}>
            Agregar Proveedor
          </BigButton>
        </Box>
      </Box>
    </>
  )
}

export default SuppliersPage
