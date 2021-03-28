import React from 'react'
import { StyleSheet, Text, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import Menu from './components/Menu';

const Home = () => {
    return (
        <>
        <Menu />
        <View style={styles.container}>
            <Text>Home</Text>
          <StatusBar style="auto" />
        </View>
        </>
      );
}

export default Home

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
});