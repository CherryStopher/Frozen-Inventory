import { useState } from 'react'
import {
  Box,
  Typography,
  Modal,
  Paper,
  Button,
  MenuItem,
  TextField
} from '@mui/material'
import { useTheme } from '@mui/material/styles'
import styles from './AddProductModal.module.css'

interface AddProductModalProps {
  open: boolean
  handleClose: () => void
}

export const AddProductModal: React.FC<AddProductModalProps> = ({
  open,
  handleClose
}: AddProductModalProps) => {
  const theme = useTheme()
  const [showConfirmation, setShowConfirmation] = useState(false)
  const [enteredProductName, setEnteredProductName] = useState<string>('')
  const [productName, setProductName] = useState<string>('')
  const [productQuantity, setProductQuantity] = useState<string>('')
  const [productUnit, setProductUnit] = useState<string>('Kg')
  const [productSupplier, setProductSupplier] = useState<string>('')
  const [productCategory, setProductCategory] = useState<string>('Congelados')
  const [productPrice, setProductPrice] = useState<string>('')
  const resetInputs = (): void => {
    setProductName('')
    setProductQuantity('')
    setProductUnit('Kg')
    setProductSupplier('')
    setProductCategory('Congelados')
    setProductPrice('')
  }
  const handleSubmit = (): void => {
    setEnteredProductName(productName)
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
        <Typography variant="h4" component="h2" className={styles.modalTitle}>
          Ingreso de nuevo producto
        </Typography>
        <Paper className={styles.formContainer}>
          <Box className={styles.inputContainer}>
            <TextField
              label={'Producto'}
              value={productName}
              fullWidth
              onChange={(e) => {
                setProductName(e.target.value)
              }}
            />
          </Box>
          <Box className={styles.inputContainer}>
            <Box className={styles.horizontalContainer}>
              <TextField
                label={'Cantidad'}
                value={productQuantity}
                type="number"
                onChange={(e) => {
                  setProductQuantity(e.target.value)
                }}
              />
              <TextField
                label={'Unidad'}
                value={productUnit}
                defaultValue={'L'}
                select
                className={styles.unitInput}
                onChange={(e) => {
                  setProductUnit(e.target.value)
                }}
              >
                <MenuItem key={'Kg'} value={'Kg'}>
                  Kg
                </MenuItem>
                <MenuItem key={'L'} value={'L'}>
                  L
                </MenuItem>
                <MenuItem key={'Unidad'} value={'Unidad'}>
                  Unidad
                </MenuItem>
              </TextField>
            </Box>
          </Box>
          <Box className={styles.inputContainer}>
            <Box className={styles.horizontalContainer}>
              <TextField
                label={'Proveedor'}
                value={productSupplier}
                defaultValue={'L'}
                select
                className={styles.supplierInput}
                onChange={(e) => {
                  setProductSupplier(e.target.value)
                }}
              >
                <MenuItem key={'Minuto Verde'} value={'Minuto Verde'}>
                  Minuto Verde
                </MenuItem>
                <MenuItem key={'Agrosuper'} value={'Agrosuper'}>
                  Agrosuper
                </MenuItem>
                <MenuItem key={'Guallarauco'} value={'Guallarauco'}>
                  Guallarauco
                </MenuItem>
              </TextField>
              <TextField
                label={'Categoría'}
                value={productCategory}
                select
                className={styles.categoryInput}
                onChange={(e) => {
                  setProductCategory(e.target.value)
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
            <TextField
              label={'Precio de venta'}
              value={productPrice}
              onChange={(e) => {
                setProductPrice(e.target.value)
              }}
            />
          </Box>
          <Box className={styles.buttonContainer}>
            <Button onClick={handleSubmit} className={styles.submitButton}
              style={{
                backgroundColor: theme.palette.primary.main,
                color: theme.colors.white
              }}>
              Ingresar
            </Button>
          </Box>
        </Paper>
        {showConfirmation && (
          <Box style={{
            backgroundColor: theme.palette.success.main,
            color: theme.palette.success.contrastText,
            padding: '8px'
          }}>
            <Typography
              variant="h6"
              component="h3"
              className={styles.confirmationText}
            >
              Se ha ingresado correctamente {enteredProductName}.
            </Typography>
          </Box>
        )}
      </Box>
    </Modal>
  )
}
