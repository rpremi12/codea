import Image from 'next/image';
import Logo from '../assets/codea-logo.svg'


export default function Navbar() {
    return(
        <nav className="navbar">
            <Image
            src={Logo}
            alt="Codea" />
        </nav>
    )
}