import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const Menu = () => {
  return (
  <View style={styles.container} >
    <Text>Componentes</Text>
    </View>
    )
}

export default Menu;

const styles = StyleSheet.create({
  container: {
    height: 80,
    backgroundColor: '#E48040',
    alignItems: 'center',
    justifyContent: 'center',
  },
});