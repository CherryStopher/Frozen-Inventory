import { FormEvent } from 'react';

export const preventSubmit = (e: FormEvent<HTMLFormElement>): void => {
  e.preventDefault();
};