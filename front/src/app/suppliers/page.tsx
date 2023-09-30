'use client'
import { useState, useMemo, useEffect } from 'react'
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
import { useAxios } from '@hooks/useAxios'
import styles from './page.module.css'


const tableSort: Sortable = {
  defaultValue: {
    column: 'fantasyName',
    order: 'desc'
  }
}

const suppliersCols: CustomTableColumn[] = [
  {
    title: 'Proveedor',
    attr: 'fantasyName'
  },
  {
    title: 'Razón Social',
    attr: 'businessName'
  },
  {
    title: 'Nombre contacto',
    attr: 'contactName'
  },
  {
    title: 'Proveedor',
    attr: 'rut'
  },
  {
    title: 'Teléfono',
    attr: 'phone'
  },
  {
    title: 'Correo',
    attr: 'email'
  },
]

const fuseOptions = {
  keys: ['name', 'category']
}

const SuppliersPage = (): JSX.Element => {
  const theme = useTheme()
  const [searchText, setSearchText] = useState<string>('')
  const [openModal, setOpenModal] = useState(false)
  const [filteredSuppliers, setFilteredSuppliers] = useState<Supplier[]>([])
  const [loading, error, suppliersData] = useAxios<Supplier[]>('/suppliers/get_all', 'GET', {})

  useEffect(() => {
    if (suppliersData) {
      if (searchText.length < 2) {
        setFilteredSuppliers(suppliersData);
      } else {
        const fuse = new Fuse(suppliersData, fuseOptions);
        const results = fuse.search(searchText).map((result) => result.item);
        setFilteredSuppliers(results);
      }
    }
  }, [searchText, suppliersData]);

  const tableSuppliers: CustomTableRow[] = useMemo(() => {
    return filteredSuppliers.map((supplier) => ({
      data: {
        fantasyName: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.fantasyName
        },
        businessName: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.businessName
        },
        contactName: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.contactName
        },
        rut: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.rut
        },
        phone: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.phone
        },
        email: {
          type: CustomTableRowDataType.TEXT,
          text: supplier.email
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
            columns={suppliersCols}
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
