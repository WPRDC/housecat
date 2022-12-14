import '../styles/globals.css';
import type { AppProps } from 'next/app';

import { Provider } from '@wprdc-components/provider';
import Layout from '../components/Layout';
import { ReactElement, ReactNode } from 'react';
import { NextPage } from 'next';
import { QueryClient } from 'react-query';

import { SSRProvider } from 'react-aria';

import 'mapbox-gl/dist/mapbox-gl.css';

type NextPageWithLayout = NextPage & {
  getLayout?: (page: ReactElement) => ReactNode;
};

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout;
};

const queryClient = new QueryClient();

const MAPBOX_KEY = process.env.NEXT_PUBLIC_MAPBOX_API_KEY;
const API_HOST = process.env.NEXT_PUBLIC_API_HOST || undefined;

console.debug({
  API_HOST,
});

function MyApp({ Component, pageProps }: AppPropsWithLayout) {
  // default layout is components/Layout
  const getLayout =
    Component.getLayout ?? ((page) => <Layout protect>{page}</Layout>);
  return (
    <Provider
      usingSSR
      mapboxAPIToken={MAPBOX_KEY}
      queryClient={queryClient}
      housecatHost={API_HOST}
    >
      <SSRProvider>{getLayout(<Component {...pageProps} />)}</SSRProvider>
    </Provider>
  );
}

export default MyApp;
