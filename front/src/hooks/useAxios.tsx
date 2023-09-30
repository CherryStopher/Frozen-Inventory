import { useEffect, useState } from 'react';
import axios, { Method } from 'axios';
import { snakeToCamel, convertKeysToCamelCase } from '@utils/strings';

const apiUrl: string | undefined = process.env.NEXT_PUBLIC_API_URL

function useAxios<T>(
  query: string,
  method: Method,
  body: any
): [boolean, string | null, T | null] {
  const [loading, setLoading] = useState<boolean>(false);
  const [returnData, setReturnData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  const url = `${apiUrl}${query}`

  useEffect(() => {
    setLoading(true);

    const fetchData = async (): Promise<void> => {
      try {
        const response = await axios({
          url,
          method,
          data: body,
        });

        const responseData = response?.data;

        if (responseData !== undefined && responseData !== null) {
          if (Array.isArray(responseData)) { // Response is an array
            const camelCasedList = responseData.map((item: any) =>
              convertKeysToCamelCase(item)
            );
            setReturnData(camelCasedList as T);
          } else if (typeof responseData === 'object') { // Response is an object
            const camelCasedObject = convertKeysToCamelCase(responseData);
            setReturnData(camelCasedObject as T);
          } else {
            setReturnData(responseData as T);
          }
        } else {
          setReturnData(null);
        }
      } catch (error: any) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    void fetchData();
  }, [query, method]);

  return [loading, error, returnData];
}

export { useAxios };