'use client'
import { useState } from 'react'
import {
  Box,
  Typography,
  Modal,
  Paper,
  Button,
  MenuItem,
  TextField,
  InputAdornment
} from '@mui/material'
import { useTheme } from '@mui/material/styles'
import styles from './AddSupplierModal.module.css'

interface AddSupplierModalProps {
  open: boolean
  handleClose: () => void
}

export const AddSupplierModal: React.FC<AddSupplierModalProps> = ({
  open,
  handleClose
}: AddSupplierModalProps) => {
  const theme = useTheme()
  const [showConfirmation, setShowConfirmation] = useState(false)
  const [enteredSupplierName, setEnteredSupplierName] = useState<string>('')
  const [supplierName, setSupplierName] = useState<string>('')
  const [supplierContact, setSupplierContact] = useState<string>('')
  const [supplierCategory, setSupplierCategory] = useState<string>('')
  const [supplierEmail, setSupplierEmail] = useState<string>('')
  const [supplierPhone, setSupplierPhone] = useState<string>('')
  const [supplierCommune, setSupplierCommune] = useState<string>('')
  const [supplierAddress, setSupplierAddress] = useState<string>('')
  const resetInputs = (): void => {
    setSupplierName('')
    setSupplierContact('')
    setSupplierCategory('Abarrotes')
    setSupplierEmail('')
    setSupplierPhone('')
    setSupplierCommune('')
    setSupplierAddress('')
  }
  const handleSubmit = (): void => {
    setEnteredSupplierName(supplierName)
    setShowConfirmation(true)
    resetInputs()
  }
  const handleCloseModal = (): void => {
    setShowConfirmation(false)
    handleClose()
  }

  return (
    <Modal open={open} onClose={handleCloseModal}>
      <Box className={styles.modalContainer}
      sx={{
        bgcolor: 'background.paper'
      }}>
        <Typography variant="h4" component="h2">
          Ingreso de nuevo proveedor
        </Typography>
        <Paper className={styles.formContainer}>
          <Box className={styles.inputContainer}>
            <TextField
              label={'Proveedor'}
              value={supplierName}
              fullWidth
              onChange={(e) => {
                setSupplierName(e.target.value)
              }}
            />
          </Box>
          <Box className={styles.inputContainer}>
            <Box className={styles.horizontalContainer}>
              <TextField
                label={'Nombre contacto'}
                value={supplierContact}
                className={styles.supplierInput}
                onChange={(e) => {
                  setSupplierContact(e.target.value)
                }}
              ></TextField>
              <TextField
                label={'Categoría'}
                value={supplierCategory}
                select
                className={styles.categoryInput}
                onChange={(e) => {
                  setSupplierCategory(e.target.value)
                }}
              >
                <MenuItem key={'Abarrotes'} value={'Abarrotes'}>
                  Abarrotes
                </MenuItem>
                <MenuItem key={'Congelados'} value={'Congelados'}>
                  Congelados
                </MenuItem>
                <MenuItem key={'Otros'} value={'Otros'}>
                  Otros
                </MenuItem>
              </TextField>
            </Box>
          </Box>
          <Box className={styles.inputContainer}>
            <Box className={styles.horizontalContainer}>
              <TextField
                label={'Correo'}
                value={supplierEmail}
                className={styles.emailInput}
                type="email"
                placeholder="correo@gmail.com"
                onChange={(e) => {
                  setSupplierEmail(e.target.value)
                }}
              ></TextField>
              <TextField
                label={'Teléfono'}
                value={supplierPhone}
                className={styles.phoneInput}
                sx={{
                  input: {
                    '&[type=number]': {
                      '-moz-appearance': 'textfield'
                    },
                    '&::-webkit-outer-spin-button': {
                      '-webkit-appearance': 'none',
                      margin: 0
                    },
                    '&::-webkit-inner-spin-button': {
                      '-webkit-appearance': 'none',
                      margin: 0
                    }
                  }
                }}
                onChange={(e) => {
                  setSupplierPhone(e.target.value)
                }}
                type="tel"
                placeholder="912345678"
                inputProps={{
                  maxLength: 9
                }}
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">+56 </InputAdornment>
                  )
                }}
              ></TextField>
            </Box>
          </Box>
          <Box className={styles.inputContainer}>
            <Box className={styles.horizontalContainer}>
              <TextField
                label={'Comuna'}
                value={supplierCommune}
                onChange={(e) => {
                  setSupplierCommune(e.target.value)
                }}
              ></TextField>
              <TextField
                label={'Dirección'}
                value={supplierAddress}
                className={styles.addressInput}
                onChange={(e) => {
                  setSupplierAddress(e.target.value)
                }}
              ></TextField>
            </Box>
          </Box>
          <Box className={styles.buttonContainer}>
            <Button className={styles.submitButton} onClick={handleSubmit}
              style={{
                backgroundColor: theme.palette.primary.main,
                color: theme.palette.primary.contrastText
              }}>
              Ingresar
            </Button>
          </Box>
        </Paper>
        {showConfirmation && (
          <Box className={styles.confirmationContainer}
            sx={{
              bgColor: theme.palette.success.main,
              color: theme.palette.success.contrastText
            }}>
            <Typography
              variant="h6"
              component="h3"
              className={styles.confirmationText}
            >
              Se ha ingresado correctamente {enteredSupplierName}.
            </Typography>
          </Box>
        )}
      </Box>
    </Modal>
  )
}
