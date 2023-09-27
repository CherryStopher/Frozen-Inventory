import { useState, useEffect } from 'react'
import axios, { type Method } from 'axios'

const useAxios = (
  url: string,
  method: Method,
  body: any
): [boolean, string | null, any] => {
  const [loading, setLoading] = useState<boolean>(false)
  const [data, setData] = useState<any>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    setLoading(true)
    const fetchData = async (): Promise<void> => {
      try {
        const response = await axios({
          url,
          method,
          data: body
        })
        const responseData = response?.data
        setData(responseData)
      } catch (error: any) {
        setError(error)
      } finally {
        setLoading(false)
      }
    }
    void fetchData()
  }, [url])

  return [loading, error, data]
}

export { useAxios }
