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
import { AddProductModal } from '@components/inventory'
import { type Product } from '@interfaces/index'
import Link from 'next/link'
import styles from './page.module.css'
import Fuse from 'fuse.js'
import { useAxios } from '@hooks/useAxios'

const tableSort: Sortable = {
  defaultValue: {
    column: 'name',
    order: 'asc'
  }
}

const inventoryCols: CustomTableColumn[] = [
  {
    title: 'Producto',
    attr: 'name'
  },
  {
    title: 'Unidad',
    attr: 'unit'
  },
  {
    title: 'Disponible',
    attr: 'available'
  },
  {
    title: 'Proveedor',
    attr: 'supplier'
  },
  {
    title: 'Categoría',
    attr: 'category'
  },
  {
    title: 'Costo promedio',
    attr: 'avgCost'
  },
  {
    title: 'Precio sugerido',
    attr: 'suggestedPrice'
  },
  {
    title: 'Precio de venta',
    attr: 'salePrice'
  }
]

const productsData: Product[] = [
  {
    id: 1,
    name: 'Choclo grano',
    unit: '500g',
    available: 10,
    avgCost: 890,
    suggestedPrice: 1000,
    salePrice: 1100,
    supplier: 'Minuto Verde',
    category: 'Congelados'
  },
  {
    id: 2,
    name: 'Choclo grano',
    unit: '500g',
    available: 10,
    avgCost: 890,
    suggestedPrice: 1000,
    salePrice: 1100,
    supplier: 'Minuto Verde',
    category: 'Congelados'
  },
  {
    id: 3,
    name: 'Choclo grano',
    unit: '500g',
    available: 10,
    avgCost: 890,
    suggestedPrice: 1000,
    salePrice: 1100,
    supplier: 'Minuto Verde',
    category: 'Congelados'
  },
  {
    id: 4,
    name: 'Choclo grano',
    unit: '500g',
    available: 10,
    avgCost: 890,
    suggestedPrice: 1000,
    salePrice: 1100,
    supplier: 'Minuto Verde',
    category: 'Congelados'
  },
  {
    id: 5,
    name: 'Choclo grano',
    unit: '500g',
    available: 10,
    avgCost: 890,
    suggestedPrice: 1000,
    salePrice: 1100,
    supplier: 'Minuto Verde',
    category: 'Congelados'
  },
  {
    id: 6,
    name: 'Choclo grano',
    unit: '500g',
    available: 10,
    avgCost: 890,
    suggestedPrice: 1000,
    salePrice: 1100,
    supplier: 'Minuto Verde',
    category: 'Congelados'
  }
]

const fuseOptions = {
  keys: ['name', 'supplier', 'category']
}

const InventoryPage = (): JSX.Element => {
  const [searchText, setSearchText] = useState<string>('')

  const [loading, error, data] = useAxios('/product/get/1', 'GET', {})

  const fuse = useMemo(
    () => new Fuse(productsData, fuseOptions),
    []
  )
  const [openModal, setOpenModal] = useState(false)

  const filteredProducts: Product[] = useMemo(() => {
    if (searchText.length < 2) {
      return productsData
    }
    return fuse.search(searchText).map((el) => el.item)
  }, [searchText, fuse])

  const tableProducts: CustomTableRow[] = useMemo(() => {
    return filteredProducts.map((product) => ({
      data: {
        name: {
          type: CustomTableRowDataType.TEXT,
          text: product.name
        },
        unit: {
          type: CustomTableRowDataType.TEXT,
          text: product.unit
        },
        available: {
          type: CustomTableRowDataType.TEXT,
          text: product.available.toString()
        },
        avgCost: {
          type: CustomTableRowDataType.TEXT,
          text: `$ ${product.avgCost}`
        },
        suggestedPrice: {
          type: CustomTableRowDataType.TEXT,
          text: `$ ${product.suggestedPrice}`
        },
        salePrice: {
          type: CustomTableRowDataType.TEXT,
          text: `$ ${product.salePrice}`
        },
        supplier: {
          type: CustomTableRowDataType.TEXT,
          text: product.supplier
        },
        category: {
          type: CustomTableRowDataType.TEXT,
          text: product.category
        }
      }
    }))
  }, [filteredProducts])

  return (
      <Box className={styles.root}>
        <AddProductModal
          open={openModal}
          handleClose={() => { setOpenModal(false) }}
        />
        <Paper elevation={0} className={styles.tableContainer}>
          <TableSearcher
            searchText={searchText}
            changeSearchText={setSearchText}
            placeholder={'Buscar por producto, proveedor o categoría'}
          />
          <CustomTable
            columns={inventoryCols}
            data={tableProducts}
            sortable={tableSort}
          />
        </Paper>
        <Box>
          <Box className={styles.bigButtonsContainer}>
          <BigButton onClick={() => { setOpenModal(true) }}>
              Agregar Productos
            </BigButton>
            <Link href="/suppliers" passHref>
              <BigButton onClick={() => {}}>
                Ver Proveedores
              </BigButton>
            </Link>
            <Link href="/clients" passHref>
            <BigButton onClick={() => {}}>
            {/* <BigButton onClick={() => navigate('/clients')}> */}
              Ver Clientes
            </BigButton>
            </Link>
          </Box>
        </Box>
      </Box>
  )
}

export default InventoryPage
