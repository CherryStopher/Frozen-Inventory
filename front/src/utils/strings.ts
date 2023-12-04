export const snakeToCamel = (input: string): string => {
    return input.replace(/_([a-z])/g, (match) => match[1].toUpperCase());
}

// Función para convertir las claves de un objeto a camelCase
export const convertKeysToCamelCase = (obj: any): any => {
    if (typeof obj !== 'object' || obj === null) {
      return obj;
    }

    if (Array.isArray(obj)) {
      return obj.map((item) => convertKeysToCamelCase(item));
    }

    const newObj: any = {};
    for (const key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        const newKey = snakeToCamel(key);
        newObj[newKey] = convertKeysToCamelCase(obj[key]);
      }
    }
    return newObj;
  };