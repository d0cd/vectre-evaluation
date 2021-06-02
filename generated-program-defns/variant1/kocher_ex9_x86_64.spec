prog _generated-binaries_variant1_kocher_ex9_x86_64 {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	qword ptr [rbp - 0x10], rsi;
    4194316c:	mov	rax, qword ptr [rbp - 0x10];
    4194320:	cmp	dword ptr [rax], 0;
    4194323:	je	0x400044;
ENTRY_4194372:
    4194372:	pop	rbp;
    4194373:	ret;
ENTRY_4194329:
    4194329:	mov	rax, qword ptr [rbp - 8];
    4194333d:	movzx	ecx, byte ptr [rax + 0x500000];
    4194341:	shl	ecx, 9;
    4194344:	movsxd	rax, ecx;
    4194347b:	movzx	ecx, byte ptr [rax + 0x500008];
    4194355:	movzx	edx, byte ptr [0x500010];
    4194363b:	and	edx, ecx;
    4194365d:	mov	byte ptr [0x500010], dl;
    4194372:	pop	rbp;
    4194373:	ret;
}
