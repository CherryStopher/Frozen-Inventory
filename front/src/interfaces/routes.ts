export enum AppRoute {
  INVENTORY = '/inventory',
  CLIENTS = '/clients',
  SUPPLIERS = '/suppliers',
  DAILY_SALES = '/daily-sales',
  DAILY_PURCHASES = '/daily-purchases',
}

export const AppRouteNames: Record<AppRoute, string> = {
  [AppRoute.INVENTORY]: 'Inventario',
  [AppRoute.CLIENTS]: 'Clientes',
  [AppRoute.SUPPLIERS]: 'Proveedores',
  [AppRoute.DAILY_SALES]: 'Ventas',
  [AppRoute.DAILY_PURCHASES]: 'Compras',
};

export const routeTabs = [
  AppRoute.INVENTORY,
  AppRoute.DAILY_SALES,
  AppRoute.DAILY_PURCHASES,
];

export const groupedAppRouteTabs: Record<AppRoute, AppRoute> = {
  [AppRoute.INVENTORY]: AppRoute.INVENTORY,
  [AppRoute.CLIENTS]: AppRoute.INVENTORY,
  [AppRoute.SUPPLIERS]: AppRoute.INVENTORY,
  [AppRoute.DAILY_SALES]: AppRoute.DAILY_SALES,
  [AppRoute.DAILY_PURCHASES]: AppRoute.DAILY_PURCHASES,
};
