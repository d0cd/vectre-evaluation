prog _generated-binaries_variant1_kocher_ex14_x86_64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	rax, qword ptr [rbp - 8];
    4194316c:	cmp	rax, qword ptr [0x500000];
    4194324:	jae	0x40004b;
ENTRY_4194330:
    4194330a:	mov	rax, qword ptr [rbp - 8];
    4194334e:	xor	rax, 0xff;
    4194340:	movzx	ecx, byte ptr [rax + 0x500008];
    4194348c:	shl	ecx, 9;
    4194351f:	movsxd	rax, ecx;
    4194354:	movzx	ecx, byte ptr [rax + 0x500010];
    4194362a:	movzx	edx, byte ptr [0x500018];
    4194370:	and	edx, ecx;
    4194372:	mov	byte ptr [0x500018], dl;
    4194379b:	pop	rbp;
    4194380c:	ret;
ENTRY_4194379:
    4194379b:	pop	rbp;
    4194380c:	ret;
}
