import { useNavigation } from '@react-navigation/native';
import React from 'react';
import { Image, ImageBackground, StyleSheet, Text, View } from 'react-native';
import { RectButton } from 'react-native-gesture-handler';
import Menu from '../../components/Menu'


const Home = () => {

    const navigation = useNavigation();

    function handleNavigateToPoints() {
        navigation.navigate('Points');
    }

    function handleNavigateToRegister() {
        navigation.navigate('Register');
    }

    return (
        <>
            <View>
                <View style={styles.container}>
                    <View style={styles.menu}>
                         <Menu />
                    </View>
                </View>
            </View>

        </>

    );

}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#FFF',
    },

    menu: {
        flex: 1,
        marginTop: 40,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#e48040',
    },
    box: {
        backgroundColor: '#28407C',
        width: '100%',
        height: 20,
        borderTopEndRadius: 15,
        borderTopStartRadius: 15,
    },

    centerContent: {
        marginTop: 30,
        flex: .2,
        justifyContent: 'center',
        alignItems: 'center'
    },

    title: {
        color: '#FFFFFF',
        fontSize: 32,
        fontFamily: 'Ubuntu_700Bold',
        maxWidth: 260,
        marginTop: 50,
    },

    description: {
        color: '#6C6C80',
        fontSize: 16,
        marginTop: 16,
        fontFamily: 'Roboto_400Regular',
        maxWidth: 260,
        lineHeight: 24,
    },

    footer: {
        flex: 1,
        alignItems: 'center'
    },

    img: {
        marginTop: 30,
    },
    background: {
        backgroundColor: '#0E0E0E',
    },

    // input: {
    //   height: 60,
    //   backgroundColor: '#FFF',
    //   borderRadius: 10,
    //   marginBottom: 8,
    //   paddingHorizontal: 24,
    //   fontSize: 16,
    // },

    button: {
        justifyContent: 'center',
        backgroundColor: '#28407C',
        height: 60,
        width: 250,
        flexDirection: 'row',
        borderRadius: 30,
        overflow: 'hidden',
        alignItems: 'center',
        marginTop: 8,
    },

    buttonIcon: {
        height: 60,
        width: 60,
        backgroundColor: 'rgba(0, 0, 0, 0.1)',
        justifyContent: 'center',
        alignItems: 'center'
    },

    buttonText: {
        flex: 1,
        justifyContent: 'center',
        textAlign: 'center',
        color: '#FFF',
        fontFamily: 'Roboto_500Medium',
        fontSize: 16,
    }
});

export default Home;