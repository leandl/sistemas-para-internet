import { StyleSheet, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

import { PageGithub } from './src/pages/page-github';

const queryClient = new QueryClient()

export default function App() {
  return (
    <View style={styles.container}>
      <QueryClientProvider client={queryClient}>
        <StatusBar style="auto" backgroundColor="#61dafb" />
        <PageGithub username='leandl' />
      </QueryClientProvider>
    </View>
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#212121',
  },
});
