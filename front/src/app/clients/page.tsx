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
import { type Client } from '@interfaces/index'
import { AddClientModal } from '@components/clients'
import styles from './page.module.css'
import Fuse from 'fuse.js'
import { useTheme } from '@mui/material/styles'

const tableSort: Sortable = {
  defaultValue: {
    column: 'name',
    order: 'desc'
  }
}

const inventoryCols: CustomTableColumn[] = [
  {
    title: 'Nombre',
    attr: 'name'
  },
  {
    title: 'Apodo',
    attr: 'nickname'
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
    title: 'Comuna',
    attr: 'commune'
  },
  {
    title: 'Dirección',
    attr: 'address'
  }
]

const clientsData: Client[] = [
  {
    id: 1,
    name: 'Angélica de Los Ángeles Pérez',
    nickname: 'Doña Angélica La Estrella',
    phone: '+569 1234 5678',
    email: 'angelica123@gmail.com',
    commune: 'La Estrella',
    address: 'Av. Cachapoal #164'
  }
]

const fuseOptions = {
  keys: ['name', 'nickname, commune']
}

const ClientsPage = (): JSX.Element => {
  const theme = useTheme()
  const [openModal, setOpenModal] = useState(false)

  const [searchText, setSearchText] = useState<string>('')
  const fuse = useMemo(() => new Fuse(clientsData, fuseOptions), [])
  const filteredClients: Client[] = useMemo(() => {
    if (searchText.length < 2) {
      return clientsData
    }
    return fuse.search(searchText).map((el) => el.item)
  }, [searchText, fuse])
  const tableClients: CustomTableRow[] = useMemo(() => {
    return filteredClients.map((clients) => ({
      data: {
        name: {
          type: CustomTableRowDataType.TEXT,
          text: clients.name
        },
        nickname: {
          type: CustomTableRowDataType.TEXT,
          text: clients.nickname
        },
        phone: {
          type: CustomTableRowDataType.TEXT,
          text: clients.phone
        },
        email: {
          type: CustomTableRowDataType.TEXT,
          text: clients.email
        },
        commune: {
          type: CustomTableRowDataType.TEXT,
          text: clients.commune
        },
        address: {
          type: CustomTableRowDataType.TEXT,
          text: clients.address
        }
      }
    }))
  }, [filteredClients])
  return (
    <>
      <Box className={styles.root}
      sx={{
        backgroundColor: theme.palette.background.default
      }}>
        <AddClientModal
          open={openModal}
          handleClose={() => { setOpenModal(false) }}
        />
        <Paper className={styles.tableContainer}elevation={0}>
          <TableSearcher
            searchText={searchText}
            changeSearchText={setSearchText}
            placeholder={'Buscar por nombre, apodo o comuna'}
          />
          <CustomTable
            columns={inventoryCols}
            data={tableClients}
            sortable={tableSort}
          />
        </Paper>
        <Box className={styles.bigButtonsContainer}>
          <BigButton onClick={() => { setOpenModal(true) }}>
            Agregar Cliente
          </BigButton>
        </Box>
      </Box>
    </>
  )
}

export default ClientsPage
