'use client'
import { useState } from 'react'
import {
  Box,
  Typography,
  Modal,
  Paper,
  Button,
  TextField,
  InputAdornment
} from '@mui/material'
import { useTheme } from '@mui/material/styles'
import styles from './AddClientModal.module.css'

interface AddClientModalProps {
  open: boolean
  handleClose: () => void
}

export const AddClientModal: React.FC<AddClientModalProps> = ({
  open,
  handleClose
}: AddClientModalProps) => {
  const theme = useTheme()
  const [showConfirmation, setShowConfirmation] = useState(false)
  const [enteredClientName, setEnteredClientName] = useState<string>('')
  const [clientName, setClientName] = useState<string>('')
  const [clientNickname, setClientNickname] = useState<string>('')
  const [clientEmail, setClientEmail] = useState<string>('')
  const [clientPhone, setClientPhone] = useState<string>('')
  const [clientCommune, setClientCommune] = useState<string>('')
  const [clientAddress, setClientAddress] = useState<string>('')

  const resetInputs = (): void => {
    setClientName('')
    setClientNickname('')
    setClientEmail('')
    setClientPhone('')
    setClientCommune('')
    setClientAddress('')
  }
  const handleSubmit = (): void => {
    setEnteredClientName(clientName)
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
          Ingreso de nuevo cliente
        </Typography>
        <Paper className={styles.formContainer}>
          <Box className={styles.inputContainer}>
            <TextField
              label={'Cliente'}
              value={clientName}
              fullWidth
              onChange={(e) => {
                setClientName(e.target.value)
              }}
            />
          </Box>
          <Box className={styles.inputContainer}>
            <TextField
              label={'Apodo'}
              value={clientNickname}
              fullWidth
              onChange={(e) => {
                setClientNickname(e.target.value)
              }}
            />
          </Box>
          <Box className={styles.inputContainer}>
            <Box className={styles.horizontalContainer}>
              <TextField
                label={'Correo'}
                value={clientEmail}
                className={styles.emailInput}
                type="email"
                placeholder="correo@gmail.com"
                onChange={(e) => {
                  setClientEmail(e.target.value)
                }}
              ></TextField>
              <TextField
                label={'Teléfono'}
                value={clientPhone}
                className={styles.phoneInput}
                sx= {{
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
                  setClientPhone(e.target.value)
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
                value={clientCommune}
                onChange={(e) => {
                  setClientCommune(e.target.value)
                }}
              ></TextField>
              <TextField
                label={'Dirección'}
                value={clientAddress}
                className={styles.addressInput}
                onChange={(e) => {
                  setClientAddress(e.target.value)
                }}
              ></TextField>
            </Box>
          </Box>
          <Box className={styles.buttonContainer}>
            <Button className={styles.submitButton} onClick={handleSubmit}
              sx= {{
                bagColor: theme.palette.primary.main,
                color: theme.palette.primary.contrastText,
                '&:hover': {
                  bagColor: theme.palette.primary.dark
                }
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
              Se ha ingresado correctamente {enteredClientName}.
            </Typography>
          </Box>
        )}
      </Box>
    </Modal>
  )
}
